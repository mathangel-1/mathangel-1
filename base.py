import streamlit as st

def create_groups(male_count, female_count, num_groups=5):
    total_students = male_count + female_count

    # 학생 수를 그룹 수로 나눈 후 각 그룹에 할당할 남학생과 여학생 수 계산
    base_males_per_group = male_count // num_groups
    base_females_per_group = female_count // num_groups

    males_remainder = male_count % num_groups
    females_remainder = female_count % num_groups

    groups = []

    for i in range(num_groups):
        males_in_group = base_males_per_group + (1 if i < males_remainder else 0)
        females_in_group = base_females_per_group + (1 if i < females_remainder else 0)
        groups.append((males_in_group, females_in_group))

    return groups

# Streamlit 앱 시작
st.title("학생 그룹 나누기")

# 사용자가 남학생과 여학생 수를 입력
male_count = st.number_input("남학생 수를 입력하세요:", min_value=0, value=0)
female_count = st.number_input("여학생 수를 입력하세요:", min_value=0, value=0)

if st.button("그룹 나누기"):
    if male_count + female_count == 0:
        st.warning("남학생과 여학생 수를 입력하세요.")
    else:
        groups = create_groups(male_count, female_count)
        st.write("학생들은 다음과 같이 그룹으로 나누어집니다:")

        for i, (males, females) in enumerate(groups):
            total = males + females
            st.write(f"그룹 {i + 1}: 남학생 {males}명, 여학생 {females}명, 총 {total}명")