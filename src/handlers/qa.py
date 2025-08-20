from aiogram import Router, types
from aiogram.filters import Command
import requests
import os

router = Router()

@router.message(Command("question"))
async def on_question(msg: types.Message):
    if len(msg.text.split()) < 2:
        await msg.answer("❓ **Ask me anything!**\n\nExample: `/question What is photosynthesis?`\n\nExample: `/question Explain Newton's laws of motion`\n\nExample: `/question Assam history important dates`", parse_mode="Markdown")
        return
    
    question = msg.text.split(' ', 1)[1]
    await msg.answer(f"🤔 **Question:**_{question}_\n\n🔍 Researching answer...", parse_mode="Markdown")
    
    try:
        # Add OpenAI API integration here
        openai_key = os.getenv("OPENAI_API_KEY")
        
        if openai_key:
            # OpenAI API call
            headers = {
                "Authorization": f"Bearer {openai_key}",
                "Content-Type": "application/json"
            }
            
            data = {
                "model": "gpt-3.5-turbo",
                "messages": [{"role": "user", "content": question}],
                "max_tokens": 500
            }
            
            response = requests.post(
                "https://api.openai.com/v1/chat/completions",
                headers=headers,
                json=data,
                timeout=30
            )
            
            if response.status_code == 200:
                answer = response.json()["choices"][0]["message"]["content"]
                response_text = f"💡 **Answer:**\n\n{answer}"
            else:
                response_text = "⚠️ Could not generate answer. Please try again later."
        
        else:
            # Fallback without API key
            response_text = f"✅ **Question received:**_{question}_\n\n📚 I'll help you find the answer from educational resources!\n\nTry searching PDFs first: `/pdf {question}`", parse_mode="Markdown"
        
        await msg.answer(response_text, parse_mode="Markdown")
        
    except Exception as e:
        await msg.answer(f"❌ Error: {str(e)}")