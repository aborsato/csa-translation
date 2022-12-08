# Azure Cognitive Services Translation demo

from [Microsoft Learn](https://learn.microsoft.com/en-us/azure/cognitive-services/translator/quickstart-translator?tabs=python):

Try the latest version of Azure Translator. In this quickstart, you'll get started using the Translator service to translate text using a programming language of your choice or the REST API. For this project, we recommend using the free pricing tier (F0), while you're learning the technology, and later upgrading to a paid tier for production.

## Run

1. Create a file `.env` at the root folder (follow instructions on how to retrieve the keys in the link above):
   ```env
   TRANSLATOR_KEY=xxxxxxxxxxxxxxxxxxxxxxxxx
   TRANSLATOR_ENDPOINT=https://api.cognitive.microsofttranslator.com
   TRANSLATOR_LOCATION=YOUR_TRANSLATOR_SERVICE_LOCATION
   ```
1. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
1. Run the sample code:
   ```bash
   python main.py
   ```

Alternatively, you can run it from bash command line:
```bash
source .env
# Pass secret key and region using headers to a custom endpoint
curl -X POST "$TRANSLATOR_ENDPOINT/translate?api-version=3.0&from=en&to=fr&to=es&to=pt" \
-H "Ocp-Apim-Subscription-Key: $TRANSLATOR_KEY" \
-H "Ocp-Apim-Subscription-Region: $TRANSLATOR_LOCATION" \
-H "Content-Type: application/json" \
-d "[{'Text':'Hello'}]" -v | jq
```
the result will look like this:
```json
[
  {
    "translations": [
      {
        "text": "Bonjour",
        "to": "fr"
      },
      {
        "text": "Hola",
        "to": "es"
      },
      {
        "text": "Olá",
        "to": "pt"
      }
    ]
  }
]
```
