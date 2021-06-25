# Copyright 2021 Google LLC
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#    http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

# [START translate_v3beta1_translate_document]
from google.cloud import translate_v3beta1 as translate


def translate_document(project_id: str, file_path: str):
    '''Translating a Document'''

    client = translate.TranslationServiceClient()

    location = "us-central1"

    parent = f"projects/{project_id}/locations/{location}"

    with open(file_path, "rb") as document:
        document_content = document.read()

    document_input_config = {
        "content": document_content,
        "mime_type": "application/pdf",
    }

    response = client.translate_document(
        request={
            "parent": parent,
            "target_language_code": "fr-FR",
            "document_input_config": document_input_config,
        }
    )

    '''
    To view translated document, write `response.document_translation.byte_stream_outputs` to file.
    '''
    print("Response: Detected Language Code - {}".format(response.document_translation.detected_language_code))


# [END translate_v3beta1_translate_document]
