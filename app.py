import gradio as gr
from TTS.api import TTS
import torch
import os

# التحقق من توفر كرت الشاشة لتسريع العملية في الكولاب
device = "cuda" if torch.cuda.is_available() else "cpu"
print(f"Using device: {device}")

# تحميل نموذج استنساخ وتوليد الصوت الاحترافي الثقيل
print("Loading XTTS-v2 model...")
tts = TTS("tts_models/multilingual/multi-dataset/xtts_v2").to(device)

def clone_voice(text, audio_file):
    if not text.strip():
        return "الرجاء إدخال نص صحيح."
    if not audio_file:
        return "الرجاء رفع عينة صوتية للاستنساخ."
    
    output_path = "output_cloned.wav"
    
    try:
        # تنفيذ عملية الاستنساخ والتوليد
        tts.tts_to_file(
            text=text,
            file_path=output_path,
            speaker_wav=audio_file,
            language="ar"
        )
        return output_path
    except Exception as e:
        return f"حدث خطأ: {str(e)}"

# بناء واجهة الموقع الاحترافية باستخدام Gradio
with gr.Blocks(theme=gr.themes.Soft()) as demo:
    gr.Markdown("# 🎙️ منصة استنساخ وتوليد الصوت الاحترافية (AI Voice Cloner)")
    gr.Markdown("قم برفع ملف صوتي لشخصية تريد استنساخ صوته (مدة العينة 5-10 ثواني بصيغة WAV أو MP3)، واكتب النص المراد نطقه.")
    
    with gr.Row():
        with gr.Column():
            text_input = gr.Textbox(
                label="النص المراد توليده بالصوت المستنسخ (باللغة العربية)", 
                placeholder="اكتب هنا...", 
                lines=4
            )
            audio_input = gr.Audio(
                label="عينة الصوت المرجعية للاستنساخ (Reference Audio)", 
                type="filepath"
            )
            generate_btn = gr.Button("بدء الاستنساخ والتوليد 🚀", variant="primary")

        
        with gr.Column():
            audio_output = gr.Audio(
                label="النتيجة الصوتية النهائية", 
                type="filepath"
            )

    generate_btn.click(
        fn=clone_voice, 
        inputs=[text_input, audio_input], 
        outputs=audio_output
    )

if __name__ == "__main__":
    # تشغيل الواجهة وفتح رابط مباشر
    demo.launch(share=True, debug=True)
