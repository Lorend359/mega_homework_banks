# from src.masks import get_mask_card_number, get_mask_account
from src.processing import result_filter_by_state, result_sort_by_date
from src.widget import get_date, mask_account_card

# print(get_mask_card_number((input())))
# print(get_mask_account((input())))
print(mask_account_card(input()))
print(get_date("2024-03-11T02:26:18.671407"))
# print(result_filter_by_state)
# print(result_sort_by_date)