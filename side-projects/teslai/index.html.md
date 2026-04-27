# TeslAI

> A multilingual Nikola Tesla visitor guide built for Turistička zajednica grada Karlovca, with QR-based local suggestions and text-only answers.

Canonical page: https://dragutinoreski.com/side-projects/teslai/

Live app: https://teslai.netlify.app/

## What It Is

TeslAI is a public visitor-facing app created for Turistička zajednica grada Karlovca / Karlovac Tourist Board.

The goal was to help people discover the area through a more conversational experience: visitors scan a QR code, open the app in a location-specific context, and ask Tesla about nearby places, restaurants, activities, accommodation, or practical travel details.

## Important Product Choice

The project was originally imagined as a voice-to-voice experience, but Tesla voice output was removed. Visitors can use the microphone for input, but the app always answers in text. It does not clone or synthesize Tesla's voice.

## What It Can Do

- Accept typed chat messages.
- Accept microphone input for questions.
- Answer in a Tesla-inspired persona.
- Support multiple languages, including English, Croatian, German, French, Polish, and others.
- Provide local recommendations from the tourism-board material.
- Load different greetings and suggestions depending on which QR/location entry point the visitor used.
- Keep output text-only.

## Visitor Flow

1. The visitor scans a location QR code.
2. The app opens with a greeting and suggestions tied to that location.
3. The visitor asks Tesla a question by text or microphone.
4. The app answers in text.
5. The visitor can continue with suggested follow-up questions.

## Product Notes

- The app is designed for visitors arriving from QR codes, not for users configuring a chatbot.
- The QR entry point changes the opening message and suggested questions.
- Tesla is present visually and conversationally, but without cloned voice output.
- The tourism context lets the assistant answer about local recommendations and places to visit.

## Links

- Project page: https://dragutinoreski.com/side-projects/teslai/
- Live app: https://teslai.netlify.app/
- Gospić greeting: https://teslai.netlify.app/?location=gospic
- Plitvice greeting: https://teslai.netlify.app/?location=plitvice
