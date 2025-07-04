import openai

# توکن API خودت از OpenAI رو اینجا قرار بده
openai.api_key = "your-openai-api-key"

def analyze_message(text):
    """
    تحلیل پیام فروشنده برای استخراج اطلاعات کلیدی از متن مکالمه.
    """
    try:
        prompt = f"""
        تحلیل کن این پیام رو و اطلاعات کلیدی درباره‌ی مشتری، نیازهاش، و مرحله فروش رو استخراج کن:
        
        پیام:
        \"\"\"{text}\"\"\"
        
        خروجی باید JSON باشه، با این فیلدها:
        - customer_name
        - intent (مثلاً: خرید فوری، بررسی، فقط سوال)
        - product_interest
        - next_step (مثلاً: تماس، ارسال قیمت، منتظر پاسخ)
        """

        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "تو یک CRM Assistant هستی"},
                {"role": "user", "content": prompt}
            ],
            temperature=0.4,
            max_tokens=300
        )

        content = response['choices'][0]['message']['content']
        return content

    except Exception as e:
        return f"خطا در تحلیل پیام: {str(e)}"
