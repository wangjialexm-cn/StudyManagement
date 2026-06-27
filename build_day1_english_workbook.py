import importlib.util
from docx import Document
from docx.shared import Inches, Pt


BASE_PATH = "/Users/user/Documents/家庭教师/build_five_day_english_workbook.py"
OUT = "/Users/user/Documents/家庭教师/第1天英语补缺练习.docx"

spec = importlib.util.spec_from_file_location("workbook_base", BASE_PATH)
base = importlib.util.module_from_spec(spec)
spec.loader.exec_module(base)


def build():
    doc = Document()
    base.setup_styles(doc)
    base.set_header_footer(doc.sections[0])

    base.heading(doc, "第 1 天英语补缺练习", 1)
    base.info_line(doc)
    base.callout(doc, "今日重点", "高频错词的主动拼写；一般过去时与过去进行时。建议用时 60 分钟，到点即停。不会的题可空着，不查答案。")

    base.heading(doc, "一、词汇主动拼写（建议 20 分钟）", 2)
    base.body(doc, "根据中文写出英文单词或短语。")
    base.vocab_table(doc, [
        "减少；降低", "保持；仍然", "目的；用途", "图像；形象",
        "意识到", "研究", "摧毁；破坏", "打败",
        "激动；兴奋", "可用的；有空的", "迅速的", "准备；准备工作",
    ])

    base.heading(doc, "二、用所给词的正确形式填空（建议 15 分钟）", 2)
    for q in [
        "I ________ (wash) my clothes yesterday.",
        "Lily ________ (sing) at nine yesterday evening.",
        "At that moment, Tom ________ (watch) a documentary.",
        "Long ago, people ________ (climb) the mountain to celebrate the festival.",
        "He ________ (fly) a kite with his father last Sunday.",
        "While she was cooking, her brother ________ (play) the violin.",
        "What ________ you ________ (do) last weekend?",
        "The boy ________ (realize) his mistake after the teacher talked to him.",
        "When I saw her, she ________ (make) a snowman.",
        "They ________ (complete) the project two days ago.",
    ]:
        base.numbered(doc, q)

    base.heading(doc, "三、改错（建议 10 分钟）", 2)
    base.body(doc, "每句只有一处主要错误，请写出正确句子。")
    for q in [
        "I wash my clothes yesterday.",
        "I was make a snowman at this time yesterday.",
        "She were reading when I called her.",
        "What did you did last weekend?",
        "At nine last night, he watches TV.",
    ]:
        base.numbered(doc, q, 1)

    base.heading(doc, "四、看中文写英文（建议 15 分钟）", 2)
    for q in [
        "昨天我放了风筝。",
        "昨晚九点莉莉正在唱歌。",
        "那时他正在看一部纪录片。",
        "我意识到了自己的错误。",
        "这项研究带来了快速进步。",
    ]:
        base.numbered(doc, q, 1)

    base.heading(doc, "完成后自评", 2)
    base.body(doc, "最不确定的题号：____________________    实际用时：________ 分钟")
    base.body(doc, "今天的感觉：□轻松    □合适    □稍难    □太难")

    for section in doc.sections:
        section.page_width = Inches(8.5)
        section.page_height = Inches(11)
        section.top_margin = Inches(0.72)
        section.bottom_margin = Inches(0.72)
        section.left_margin = Inches(0.8)
        section.right_margin = Inches(0.8)
        section.header_distance = Inches(0.35)
        section.footer_distance = Inches(0.35)
    doc.core_properties.title = "第1天英语补缺练习"
    doc.core_properties.subject = "中考后轻量恢复期英语练习"
    doc.core_properties.author = "Codex"
    doc.save(OUT)
    print(OUT)


if __name__ == "__main__":
    build()
