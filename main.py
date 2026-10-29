import random
import time

def russian_roulette():
    print("【俄羅斯轉盤：機器人挑戰賽】")

    money = 0
    robot_level = 1

    while True:
        players = ["真人", f"機器人 {robot_level}"]
        robot = players[1]

        print(f"\n========== 挑戰 {robot} ==========")
        print("彈夾有 6 格，每局隨機裝入 0 或 1 顆子彈。")
        print("1. 對自己開槍")
        print("2. 對對面開槍")
        print("對自己開槍且空槍：繼續行動。")
        print("對對面開槍且空槍：換對面行動。")
        print("當槍指自己且空槍獲得 100000 元。\n")

        current_player = random.choice(players)
        print(f"隨機先手：{current_player}")

        game_over = False
        loser = None
        rounds = 0

        while not game_over:
            rounds += 1

            bullet_count = random.randint(0, 1)
            bullet_slot = random.randint(1, 6) if bullet_count else None

            print(f"\n--- 第 {rounds} 回合 ---")
            for slot in range(1, 7):
                print(f"\n第 {slot} 格，輪到：{current_player}")

                if current_player == "真人":
                    while True:
                        choice = input(
                            "1. 對自己開槍  2. 對機器人開槍："
                        ).strip()

                        if choice not in {"1", "2"}:
                            print("請輸入 1 或 2。")
                            continue

                        break

                    target = "真人" if choice == "1" else robot

                else:
                    # 機器人等級越高，越常選擇攻擊對手
                    action = random.choices(
                        ["self", "opponent"],
                        weights=[max(1, 5 - robot_level),
                                    min(10, 1 + robot_level)]
                    )[0]

                    target = robot if action == "self" else "真人"
                    print(
                        f"{robot} 選擇對 {'自己' if target == robot else '你'} 開槍！"
                    )

                print("正在開槍...")
                time.sleep(0.5)

                if bullet_slot == slot:
                    print(f"{target} 被子彈擊中！")
                    loser = target
                    game_over = True
                    break

                print("空槍！")

                if target == "真人":
                    money += 100000

                print(f"{current_player} 空槍，獲得 100000 元！")
                print(f"目前你的累積獎金：{money} 元")

                # 對自己開槍，空槍後繼續
                # 對對面開槍，空槍後換人
                if target != current_player:
                    current_player = target


        if loser == robot:
            print("\n========== 本局結束 ==========")
            print(f"你的累積獎金：{money} 元")
            print(f"恭喜！你擊敗了{robot}！")
            robot_level += 1
            print(f"下一個對手：機器人 {robot_level}")
        else:
            break

    print("\n========== 最終成績 ==========")
    print(f"你總共獲得：{money} 元")
    print(f"最高擊敗機器人等級：{robot_level - 1}")


if __name__ == "__main__":
    russian_roulette()
