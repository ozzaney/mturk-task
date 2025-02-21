import boto3
import os

MTURK_SANDBOX = 'https://mturk-requester.us-east-1.amazonaws.com'

aws_access_key_id = os.getenv('AWS_ACCESS_KEY_ID')
aws_secret_access_key = os.getenv('AWS_SECRET_ACCESS_KEY')

# 자격 증명 확인
if not aws_access_key_id or not aws_secret_access_key:
    raise ValueError("AWS credentials not found. Please set AWS_ACCESS_KEY_ID and AWS_SECRET_ACCESS_KEY environment variables.")

mturk = boto3.client('mturk',
   aws_access_key_id=aws_access_key_id,
   aws_secret_access_key=aws_secret_access_key,
   region_name='us-east-1',
   endpoint_url=MTURK_SANDBOX
)

# 실제 호스팅된 URL로 교체
question = """
<ExternalQuestion xmlns="http://mechanicalturk.amazonaws.com/AWSMechanicalTurkDataSchemas/2006-07-14/ExternalQuestion.xsd">
  <ExternalURL>https://ozzaney.github.io/mturk-task/</ExternalURL>
  <FrameHeight>600</FrameHeight>
</ExternalQuestion>
"""

# HIT 설정을 실제 용도에 맞게 수정
response = mturk.create_hit(
    Title='구체적인 태스크 제목',
    Description='명확한 태스크 설명을 입력하세요',
    Keywords='관련 키워드, 쉼표로 구분',
    Reward='1.00',  # 적절한 보상 금액 설정
    MaxAssignments=100,  # 필요한 응답 수
    LifetimeInSeconds=7*24*60*60,  # 예: 7일
    AssignmentDurationInSeconds=30*60,  # 예: 30분
    Question=question
)

print("새로운 HIT가 생성되었습니다. 여기에서 확인할 수 있습니다:")
# Sandbox 환경용 URL로 수정
print("https://workersandbox.mturk.com/mturk/preview?groupId={}".format(response['HIT']['HITGroupId']))

# HIT 상태 확인
hit_id = response['HIT']['HITId']
hit_status = mturk.get_hit(HITId=hit_id)
print("HIT 상태:", hit_status['HIT']['HITStatus'])

# 제출된 응답 확인
assignments = mturk.list_assignments_for_hit(
    HITId=hit_id,
    AssignmentStatuses=['Submitted']
)

for assignment in assignments['Assignments']:
    print("Worker ID:", assignment['WorkerId'])
    print("답변:", assignment['Answer'])