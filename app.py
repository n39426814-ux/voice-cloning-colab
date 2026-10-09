from gtts import gTTS
import gradio as gr
import os

def text_to_speech(text):
    if not text.strip():
        return None, "الرجاء كتابة نص أولاً!"

    output_path = "arabic_output.mp3"
    tts = gTTS(text=text, lang='ar')
    tts.save(output_path)

    return output_path, "تم توليد الصوت بنجاح! 🎙️"

demo = gr.Interface(
    fn=text_to_speech,
    inputs=gr.Textbox(label="أدخل النص العربي هنا", lines=4, placeholder="اكتب شيئاً ليتم تحويله إلى صوت..."),
    outputs=[
        gr.Audio(label="الملف الصوتي الناتج", type="filepath"),
        gr.Textbox(label="الحالة")
    ],
    title="🌐 موقع تحويل النص إلى صوت (عربي)",
    description="اكتب النص باللغة العربية لتحويله إلى صوت واستماعه أو تحميله مباشرة."
)

if __name__ == "__main__":
    demo.launch(server_name="0.0.0.0", server_port=7860, share=False)
