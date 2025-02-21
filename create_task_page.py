import os

# 디렉토리 생성
if not os.path.exists('mturk-task'):
    os.makedirs('mturk-task')

# index.html 생성
html_content = """
<!DOCTYPE html>
<html>
<head>
    <meta charset="UTF-8">
    <title>MTurk Task</title>
    <script src="https://assets.crowd.aws/crowd-html-elements.js"></script>
    <style>
        body { font-family: Arial, sans-serif; margin: 20px; }
        .task-container { max-width: 800px; margin: 0 auto; }
        .submit-button { 
            background-color: #4CAF50; 
            color: white; 
            padding: 10px 20px; 
            border: none; 
            border-radius: 4px; 
            cursor: pointer; 
        }
    </style>
</head>
<body>
    <crowd-form>
        <div class="task-container">
            <h1>태스크 제목</h1>
            <p>태스크 설명을 여기에 작성하세요.</p>
            
            <crowd-input name="user_input" label="답변을 입력하세요" required></crowd-input>
            
            <br><br>
            <crowd-button class="submit-button" form-action="submit">제출</crowd-button>
        </div>
    </crowd-form>

    <script>
        document.querySelector('crowd-form').onsubmit = function(e) {
            // 필요한 경우 제출 전 데이터 검증
            return true;
        };
    </script>
</body>
</html>
"""

with open('mturk-task/index.html', 'w', encoding='utf-8') as f:
    f.write(html_content)

print("파일이 생성되었습니다. 이제 GitHub에 push하세요.") 