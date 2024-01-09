def min_edit_distance(str1, str2, bonus=0):
    if not str1:
        return len(str2) * bonus
    if not str2:
        return len(str1) * bonus

    if str1[0] == str2[0]:
        cost = 0
    else:
        cost = 1

    # 插入、刪除、替換操作
    insert_cost = min_edit_distance(str1, str2[1:], bonus) + bonus
    delete_cost = min_edit_distance(str1[1:], str2, bonus) + bonus
    replace_cost = min_edit_distance(str1[1:], str2[1:], bonus) + cost

    return min(insert_cost, delete_cost, replace_cost)

# 測試例子
str1 = "kitten"
str2 = "sitting"
bonus = 2

result = min_edit_distance(str1, str2, bonus)
print(f"最小編輯距離（包含紅利）：{result}")
