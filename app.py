import gradio as gr
from TTS.api import TTS
import torch
import os

# تحميل موديل XTTS-v2 - مفتوح المصدر 100%
print("⏳ يتم تحميل XTTS-v2 لأول مرة...")
tts = TTS("tts_models/multilingual/multi-dataset/xtts_v2")
print("✅ تم التحميل")

def clone_voice(text, speaker_wav, language):
    if speaker_wav is None:
        return None, "❌ ارفع عينة صوت أولاً"
    if not text.strip():
        return None, "❌ اكتب النص"
    
    output = "/tmp/cloned.wav"
    tts.tts_to_file(
        text=text,
        speaker_wav=speaker_wav,
        language=language,
        file_path=output
    )
    return output, f"✅ تم إنتاج: {text[:30]}..."

# واجهة Gradio
with gr.Blocks(title="مصنع الصوت - XTTS-v2") as demo:
    gr.Markdown("# 🎙️ مصنع الصوت المفتوح المصدر - XTTS-v2\nيعمل على سيرفرك + Colab")
    
    with gr.Row():
        with gr.Column():
            speaker = gr.Audio(type="filepath", label="1- عينة صوتك (6 ثواني WAV)")
            lang = gr.Dropdown(choices=["ar", "en"], value="ar", label="اللغة")
            text = gr.Textbox(value="السلام عليكم، هذا صوتي من مصنعي المفتوح المصدر", label="2- النص", lines=3)
            btn = gr.Button("🔊 إنتاج صوت طبيعي قوي", variant="primary")
        
        with gr.Column():
            audio_out = gr.Audio(label="النتيجة", type="filepath")
            status = gr.Textbox(label="الحالة")
    
    btn.click(clone_voice, inputs=[text, speaker, lang], outputs=[audio_out, status])

demo.launch(server_name="0.0.0.0", server_port=7860, share=True)
