# [الخلية الأولى] - تثبيت مكتبة Coqui TTS وواجهة Gradio
!pip install -q TTS gradio

import torch
from TTS.api import TTS
import gradio as gr

# التحقق من وجود GPU
device = "cuda" if torch.cuda.is_available() else "cpu"
print(f"جاري التشغيل على جهاز: {device}")

# تحميل نموذج استنساخ الصوت XTTS v2
tts = TTS(model_name="tts_models/multilingual/multi-dataset/xtts_v2").to(device)

def clone_voice(text, audio_file):
    if not audio_file:
        return None, "يرجى تسجيل أو رفع مقطع صوتي أولاً!"
    
    output_path = "cloned_voice_output.wav"
    
    # تحويل النص إلى صوت بنفس النبرة
    tts.tts_to_file(
        text=text,
        speaker_wav=audio_file,
        language="ar",
        file_path=output_path
    )
    return output_path, "تم استنساخ الصوت بنجاح! 🎯"

# إنشاء واجهة التفاعل
iface = gr.Interface(
    fn=clone_voice,
    inputs=[
        gr.Textbox(label="النص المراد تحويله إلى صوتك", lines=4, placeholder="أدخل النص العربي هنا..."),
        gr.Audio(label="عيّنة من صوتك (سجّل من المايك أو ارفع ملف صوتي 5-10 ثوانٍ)", type="filepath")
    ],
    outputs=[
        gr.Audio(label="الملف الصوتي المستنسخ الناتج"),
        gr.Textbox(label="حالة المعالجة")
    ],
    title="🎙️ تطبيق استنساخ الصوت بالذكاء الاصطناعي",
    description="قم برفع عيّنة صوتية قصيرة لصوتك، ثم أدخل النص ليتم نطقه بأسلوب ونبرة صوتك تماماً."
)

# تشغيل التطبيق واستخراج رابط محلي وعام
iface.launch(share=True, debug=True)
