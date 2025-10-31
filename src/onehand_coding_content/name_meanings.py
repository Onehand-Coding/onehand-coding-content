"""Module to provide meanings for names using an external API."""
import os
import logging
import json
import asyncio
from typing import Optional, Dict, Any

import httpx
import pycountry
from dotenv import load_dotenv
import google.generativeai as genai

from .database import get_cached_name, cache_name

load_dotenv()
logging.basicConfig(level=logging.ERROR)


class NameMeaningProvider:
    """Provides comprehensive name analysis using an LLM as the primary source
    and external APIs as a fallback, all done asynchronously.
    """
    GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")

    def __init__(self):
        """Initialize the NameMeaningProvider."""
        self.api_urls = {
            "age": "https://api.agify.io/",
            "origin": "https://api.nationalize.io/",
            "gender": "https://api.genderize.io/"
        }
        if self.GEMINI_API_KEY:
            genai.configure(api_key=self.GEMINI_API_KEY)
            self.llm_model = genai.GenerativeModel('gemini-pro-latest')
        else:
            self.llm_model = None
            logging.warning("GEMINI_API_KEY not found. LLM features will be disabled.")

    async def analyze_name(self, name: str) -> Dict[str, Any]:
        """
        Get comprehensive information about a name asynchronously.

        This method first checks for a cached result. If not found, it
        attempts to get information from the Gemini LLM. If that fails,
        it falls back to using a combination of free APIs.
        """
        name = name.strip().title()

        # Check cache first
        cached_data = get_cached_name(name)
        if cached_data:
            cached_data['formatted_description'] = self._format_llm_description(cached_data)
            return cached_data

        # If not in cache, fetch from LLM
        llm_data = await self._fetch_from_llm(name)
        if llm_data:
            cache_name(name, llm_data)  # Cache the successful LLM response
            llm_data['formatted_description'] = self._format_llm_description(llm_data)
            return llm_data

        # Fallback to APIs if LLM fails
        logging.warning(f"Could not fetch data for '{name}' from LLM. Falling back to APIs.")
        api_data = await self._fetch_from_apis(name)
        api_data['formatted_description'] = self._format_api_description(api_data)
        return api_data

    async def _fetch_from_llm(self, name: str) -> Optional[Dict[str, Any]]:
        """
        Fetch name analysis from the Gemini LLM asynchronously.
        """
        if not self.llm_model:
            return None

        prompt = f"""
        Provide a detailed analysis of the name '{name}'. Your response MUST be a valid JSON object with the following structure:
        {{
          "name": "{name}",
          "meaning": "...",
          "origin": "...",
          "etymology": "...",
          "gender": "...",
          "famous_bearers": ["..."],
          "variations": ["..."],
          "description": "A comprehensive summary of the name's history and significance."
        }}
        Ensure the JSON is well-formed.
        """
        try:
            response = await self.llm_model.generate_content_async(prompt)
            cleaned_text = response.text.strip().replace("```json", "").replace("```", "").strip()
            return json.loads(cleaned_text)
        except (json.JSONDecodeError, Exception) as e:
            logging.error(f"Error processing LLM response for '{name}': {e}")
            return None

    async def _fetch_from_apis(self, name: str) -> Dict[str, Any]:
        """
        Fetch name information from various free APIs as a fallback, asynchronously.
        """
        result = {'name': name}
        async with httpx.AsyncClient() as client:
            tasks = [
                client.get(f"{self.api_urls['age']}?name={name}"),
                client.get(f"{self.api_urls['origin']}?name={name}"),
                client.get(f"{self.api_urls['gender']}?name={name}")
            ]
            responses = await asyncio.gather(*tasks, return_exceptions=True)

        age_response, origin_response, gender_response = responses

        if not isinstance(age_response, Exception) and age_response.status_code == 200 and 'age' in age_response.json():
            result['age_prediction'] = age_response.json()['age']

        if not isinstance(origin_response, Exception) and origin_response.status_code == 200:
            origin_data = origin_response.json().get('country', [])
            if origin_data:
                top_country_code = origin_data[0]['country_id']
                confidence = round(origin_data[0]['probability'] * 100, 2)
                country = pycountry.countries.get(alpha_2=top_country_code)
                result['origin'] = f"{country.name if country else top_country_code} (confidence: {confidence}%)"

        if not isinstance(gender_response, Exception) and gender_response.status_code == 200 and 'gender' in gender_response.json():
            gender_data = gender_response.json()
            result['gender'] = gender_data['gender'].title()
            result['gender_probability'] = round(gender_data.get('probability', 0) * 100, 2)
                
        return result

    def _format_llm_description(self, info: Dict[str, Any]) -> str:
        """
        Create a user-friendly description from the LLM name information.
        """
        name = info.get('name', 'N/A')
        parts = [f"🔍 NAME ANALYSIS: {name}"]

        if info.get('meaning'):
            parts.append(f"\n📋 MEANING: {info['meaning']}")
        if info.get('origin'):
            parts.append(f"🌍 ORIGIN: {info['origin']}")
        if info.get('etymology'):
            parts.append(f"📜 ETYMOLOGY: {info['etymology']}")
        if info.get('gender'):
            parts.append(f"⚥ GENDER: {info['gender'].title()}")
        if info.get('variations'):
            parts.append(f"🎨 VARIATIONS: {', '.join(info['variations'])}")
        if info.get('famous_bearers'):
            parts.append(f"🏆 FAMOUS BEARERS: {', '.join(info['famous_bearers'])}")
        if info.get('description'):
            parts.append(f"\n📝 DESCRIPTION:\n{info['description']}")
            
        return "\n".join(parts)

    def _format_api_description(self, info: Dict[str, Any]) -> str:
        """
        Create a user-friendly description from the API fallback data.
        """
        name = info.get('name', 'N/A')
        parts = [f"🔍 NAME ANALYSIS: {name}"]
        
        if info.get('origin'):
            parts.append(f"🌍 ORIGIN: {info['origin']}")
        if info.get('gender'):
            prob = info.get('gender_probability', 0)
            parts.append(f"⚥ GENDER PREDICTION: Most likely {info['gender']} (probability: {prob}%)")
        if info.get('age_prediction') is not None:
            parts.append(f"📅 AGE CONNECTION: Commonly associated with people around age {info['age_prediction']}")
        
        if len(parts) <= 1:
            return f"❌ No detailed information found for the name {name}. "
        
        return "\n".join(parts)


async def main():
    """Main function to test the NameMeaningProvider."""
    provider = NameMeaningProvider()
    name_to_check = "Kenneth"
    analysis = await provider.analyze_name(name_to_check)
    
    if 'formatted_description' in analysis:
        print("="*50)
        print(analysis['formatted_description'])
        print("="*50)
    else:
        print(f"Could not analyze the name '{name_to_check}'.")
        print("Raw data:", analysis)


if __name__ == '__main__':
    asyncio.run(main())
