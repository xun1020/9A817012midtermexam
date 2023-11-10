from pkg.modu import print_json, process_data, read_json, write_json

MENU_FILE = 'menu.json'       # 輸入檔案名稱
OUTPUT_FILE = 'output.json'   # 輸出檔案名稱


def main():
    # 讀取菜單
    menu = read_json(MENU_FILE)

    # 顯示原菜單
    print_json(menu)

    # 增加主菜項目
    new_main_course = {
        "name": "海鮮燉飯",
        "price": 239,
        "description": "西班牙的代表美食，海鮮配料豐富、色彩繽紛"
    }

    # 這裡修改為直接加到 "主菜" 的 "items" 中
    menu['categories'][1]['items'].append(new_main_course)

    # 讓使用者輸入折扣
    discount = float(input("請輸入折扣率(0.0 ~ 1.0): "))

    # 根據折扣打折
    process_data(menu, discount)

    # 顯示打折後菜單
    print_json(menu)

    # 寫入 output.json
    write_json(menu, OUTPUT_FILE)


if __name__ == "__main__":
    main()
