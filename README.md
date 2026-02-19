项目概览

这是一个以 pyautogui 为主的练习/工具集合，包含若干用于演示鼠标、键盘、截图、弹窗交互，以及一个基于 Excel 的自动抢课（/自动点击）脚本。

目录结构（概述）

- train_1.py .. train_16.py  —— 一组示例脚本，用来演示 pyautogui 的常见用法（移动、点击、拖拽、键盘、截图、弹窗等）。
- train_14_1.png / train_14_2.png —— 由 `train_14.py` 生成的示例截图文件。
- buildsoft_train_4/ —— 一个带简单 GUI 的鼠标位置监视器，可打包为 exe。包含：
  - create_icon.py —— 用 Pillow 生成一个简单的 ico 文件（app.ico）。
  - soft_train_4.py —— 基于 tkinter 与 pyautogui 的鼠标位置监视器（可打包为 exe）。
  - soft_train_4.exe —— 示例可执行文件（已打包版本）。
- Rushtoenrolinaclass/ —— 与“自动抢课/识别”相关的脚本与 Excel 文件：
  - auto_get_lesson_pic_recognize.py —— 读取 `info.xlsx` 并按表格指令执行自动化操作（详见下文）。
  - auto_get_lesson_pic_mecode.py —— 目前为空（待实现）。
  - info.xlsx —— 指令表（脚本读取该文件）。

主要功能分析（按文件）

- train_1.py
  - 演示绝对坐标移动：移动鼠标到 (1000,900) 并再移动到 (0,0)（最后的移动用了持续时间 2s）。

- train_2.py
  - 演示相对移动：连续调用 pi.move，带时间参数示例。

- train_3.py
  - 打印屏幕分辨率（pi.size()）和当前鼠标坐标（pi.position()）。

- train_4.py
  - 监听并打印鼠标位置的变化（循环比较并输出变动的坐标）。

- train_5.py / train_6.py / train_7.py
  - 点击与拖拽示例（单击、双击、mouseDown/mouseUp、拖拽、带延时的连续操作）。

- train_8.py
  - 点击与滚动示例（pi.click, pi.scroll）。

- train_9.py / train_10.py / train_11.py / train_12.py / train_13.py
  - 键盘输入示例：pi.write、pi.press、pi.hotkey、使用 pyperclip 复制中文并粘贴（更可靠的中文输入方案）、按键按住/释放等。

- train_14.py
  - 截图示例：保存全屏截图和裁剪截图。

- train_15.py
  - 对话框示例：pi.alert、pi.prompt 的用法。

- train_16.py
  - 一个自动化示例：模拟在编辑器中创建一个新的 Python 文件（使用点击 + prompt + 输入），演示组合流程。

- buildsoft_train_4/create_icon.py
  - 使用 Pillow 生成一个 32x32 的红色 ico 文件（app.ico）。

- buildsoft_train_4/soft_train_4.py
  - 一个小的 GUI 应用（tkinter）显示实时鼠标坐标，利用 pyautogui.position() 周期读取并更新界面。
  - 注释里给出了用 pyinstaller 打包成单文件 exe 的示例命令。

- Rushtoenrolinaclass/auto_get_lesson_pic_recognize.py（重点说明）
  - 功能：读取 `info.xlsx` 工作表（第一个 sheet），逐行按指令执行：查找屏幕上的图片并点击、粘贴字符串、等待、按热键等，支持“抢课一次”或“循环蹲点”两种模式。
  - 关键实现点：
    - 使用 `xlrd` 打开 Excel：xr = xlrd.open_workbook(filename=file)
    - 通过 sheet = xr.sheet_by_index(0) 取得第一个表单
    - 代码中遍历行的写法是：
      i = 1
      while i < sheet.nrows:
        ... sheet.cell_value(i, 1) ...
    - 说明（回答常见问题）：脚本是从 i = 1 开始遍历，也就是说它跳过了第 0 行（sheet 的第 1 行）。换句话说：脚本默认把 Excel 的第一行（索引 0）视为表头，而从第二行（索引 1）开始作为第一条执行指令。

  - 表格列约定（从代码推断）：
    - 第 2 列（索引 1）：命令类型（cmd_type），数字值：
      - 1.0 —— 左键单击（通过图像定位并点击）
      - 2.0 —— 输入字符串（通过剪贴板 + Ctrl+V）
      - 3.0 —— 等待（秒为单位）
      - 4.0 —— 键盘热键（调用 pyautogui.hotkey）
    - 第 3 列（索引 2）：命令参数：例如图像文件名（用于 locateCenterOnScreen），或字符串内容，或等待秒数，或热键名。
    - 第 4 列（索引 3）：在点击命令（cmd_type == 1）中可作为 retry 次数（可选）。

  - 运行模式：脚本运行时会打印菜单并等待输入：
    - 输入 1 —— 执行 WorkFunction1（遍历一次表格，从第二行开始执行所有指令）
    - 输入 2 —— 执行 WorkFunction2（无限循环，每次执行 WorkFunction1 后等待 2 秒，然后再执行）

  - 注意事项与建议：
    - `pyautogui.locateCenterOnScreen(img_name, confidence=0.9)` 用于按图找图，需确保截图模板与实际屏幕一致（分辨率、缩放、颜色等）。
    - `xlrd` 自 2.0 起对 xlsx 的支持被移除（只支持旧的 xls），如果 `info.xlsx` 是 .xlsx，建议安装 `openpyxl` 或降级 `xlrd==1.2.0`，或改用 pandas.read_excel / openpyxl。当前代码使用 `xlrd.open_workbook`，在现代环境中可能会报错，视你的 xlrd 版本而定。
    - 脚本使用了较高的图像匹配置信度（0.9），如果识别不到可以适当降低 confidence 值。

示例：info.xlsx 推荐表头（第一行，脚本会跳过）

| 序号 | cmd_type | 参数/内容 | retry_times(可选，用于点击) |
| --- | --- | --- | --- |
| header | header | header | header |
| 1 | 1 | button.png | 3 |
| 2 | 2 | some text to paste | |
| 3 | 3 | 2 | |
| 4 | 4 | enter | |

上面的第二行表示：找到 button.png 并点击（重试 3 次）

依赖（建议安装）

- Python 3.x
- pyautogui
- xlrd（注意版本与 xlsx 支持）或 openpyxl（如需兼容 .xlsx 可按需修改代码）
- pyperclip
- pillow（PIL，用于 create_icon.py）
- tkinter（标准库，Windows 通常自带）

安装示例：

pip install pyautogui xlrd==1.2.0 pyperclip pillow

（如果你的 info.xlsx 是.xlsx 格式并且你不希望降级 xlrd，改用 openpyxl 或 pandas 会更好）

如何使用

1. 单个演示脚本：打开命令行，在项目根目录运行：
   - python train_1.py （执行对应示例，依此类推）

2. 鼠标监视器（GUI）：
   - 进入 buildsoft_train_4，运行 python soft_train_4.py
   - 可选：先运行 create_icon.py 生成 app.ico，再使用 pyinstaller 打包：
     pyinstaller --onefile --windowed --icon=app.ico soft_train_4.py

3. 自动抢课脚本：
   - 将你准备好的 `info.xlsx` 放到 `Rushtoenrolinaclass` 文件夹（或修改脚本中的 file 变量指向路径）。
   - 运行：python auto_get_lesson_pic_recognize.py
   - 按提示输入 1（抢课一次）或 2（循环蹲点）。

已知的未实现 / 待改进项

- `Rushtoenrolinaclass/auto_get_lesson_pic_mecode.py` 文件为空，尚未实现功能。
- `auto_get_lesson_pic_recognize.py` 对 .xlsx 支持取决于本地 xlrd 版本；建议改用 `openpyxl` 或 `pandas` 来提高兼容性。
- 建议为 `info.xlsx` 添加明确表头并在 README 中保留示例模板。  
- 可以考虑添加日志功能，记录每次执行的结果（成功/失败、时间戳等），以便调试和分析。  

本代码库主要用于学习和演示 pyautogui 的功能，实际使用时请根据需要调整参数（如图像识别的 confidence）和 Excel 表格结构。对于自动化抢课等敏感操作，请确保遵守相关平台的使用政策，避免违规行为。
代码参考来源：  
- https://www.bilibili.com/video/BV1KgS3Y6Ecu/?p=17&spm_id_from=333.1007.top_right_bar_window_history.content.click
- https://zhuanlan.zhihu.com/p/444498013
