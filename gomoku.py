#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
五子棋游戏 (Gomoku / Five in a Row)
支持双人对战的命令行版本
"""


class GomokuGame:
    """五子棋游戏类"""

    def __init__(self, board_size=15):
        """
        初始化游戏
        :param board_size: 棋盘大小，默认15x15
        """
        self.board_size = board_size
        self.board = [[' ' for _ in range(board_size)] for _ in range(board_size)]
        self.current_player = 'X'  # X代表黑棋，O代表白棋
        self.move_history = []
        self.game_over = False
        self.winner = None

    def display_board(self):
        """显示棋盘"""
        print("\n   ", end="")
        # 打印列号
        for i in range(self.board_size):
            print(f"{i:2d}", end=" ")
        print("\n   " + "---" * self.board_size)

        # 打印棋盘内容
        for i in range(self.board_size):
            print(f"{i:2d}|", end=" ")
            for j in range(self.board_size):
                print(f" {self.board[i][j]}", end=" ")
            print(f"|{i:2d}")

        print("   " + "---" * self.board_size)
        print("   ", end="")
        for i in range(self.board_size):
            print(f"{i:2d}", end=" ")
        print("\n")

    def is_valid_move(self, row, col):
        """
        检查移动是否有效
        :param row: 行号
        :param col: 列号
        :return: 如果移动有效返回True，否则返回False
        """
        if row < 0 or row >= self.board_size or col < 0 or col >= self.board_size:
            return False
        if self.board[row][col] != ' ':
            return False
        return True

    def make_move(self, row, col):
        """
        执行移动
        :param row: 行号
        :param col: 列号
        :return: 如果移动成功返回True，否则返回False
        """
        if not self.is_valid_move(row, col):
            return False

        self.board[row][col] = self.current_player
        self.move_history.append((row, col, self.current_player))

        # 检查是否获胜
        if self.check_win(row, col):
            self.game_over = True
            self.winner = self.current_player
        # 检查是否平局
        elif self.is_board_full():
            self.game_over = True
            self.winner = None
        else:
            # 切换玩家
            self.current_player = 'O' if self.current_player == 'X' else 'X'

        return True

    def check_win(self, row, col):
        """
        检查是否有玩家获胜（在指定位置形成五子连珠）
        :param row: 最后一步的行号
        :param col: 最后一步的列号
        :return: 如果获胜返回True，否则返回False
        """
        directions = [
            (0, 1),   # 横向
            (1, 0),   # 纵向
            (1, 1),   # 右下斜
            (1, -1)   # 左下斜
        ]

        player = self.board[row][col]

        for dr, dc in directions:
            count = 1  # 包括当前位置

            # 正方向计数
            r, c = row + dr, col + dc
            while (0 <= r < self.board_size and
                   0 <= c < self.board_size and
                   self.board[r][c] == player):
                count += 1
                r += dr
                c += dc

            # 反方向计数
            r, c = row - dr, col - dc
            while (0 <= r < self.board_size and
                   0 <= c < self.board_size and
                   self.board[r][c] == player):
                count += 1
                r -= dr
                c -= dc

            if count >= 5:
                return True

        return False

    def is_board_full(self):
        """检查棋盘是否已满"""
        for row in self.board:
            if ' ' in row:
                return False
        return True

    def undo_move(self):
        """
        悔棋（撤销上一步）
        :return: 如果撤销成功返回True，否则返回False
        """
        if not self.move_history:
            return False

        row, col, player = self.move_history.pop()
        self.board[row][col] = ' '
        self.current_player = player
        self.game_over = False
        self.winner = None
        return True

    def reset_game(self):
        """重置游戏"""
        self.board = [[' ' for _ in range(self.board_size)] for _ in range(self.board_size)]
        self.current_player = 'X'
        self.move_history = []
        self.game_over = False
        self.winner = None


def main():
    """主函数"""
    print("=" * 50)
    print("欢迎来到五子棋游戏！")
    print("=" * 50)
    print("\n游戏规则：")
    print("1. 黑棋(X)先行，白棋(O)后行")
    print("2. 玩家轮流在棋盘上落子")
    print("3. 先将五个棋子连成一线者获胜（横、竖、斜均可）")
    print("4. 输入格式：行号 列号（例如：7 7）")
    print("5. 特殊命令：")
    print("   - 'undo' 或 'u'：悔棋")
    print("   - 'quit' 或 'q'：退出游戏")
    print("   - 'restart' 或 'r'：重新开始")
    print("=" * 50)

    # 询问棋盘大小
    while True:
        try:
            size = input("\n请输入棋盘大小（默认15，按回车使用默认值）：").strip()
            if size == '':
                board_size = 15
                break
            board_size = int(size)
            if 5 <= board_size <= 20:
                break
            else:
                print("棋盘大小应在5到20之间！")
        except ValueError:
            print("请输入有效的数字！")

    game = GomokuGame(board_size)

    # 游戏主循环
    while True:
        game.display_board()

        if game.game_over:
            if game.winner:
                player_name = "黑棋(X)" if game.winner == 'X' else "白棋(O)"
                print(f"\n🎉 恭喜！{player_name} 获胜！")
            else:
                print("\n平局！棋盘已满。")

            choice = input("\n是否再来一局？(y/n): ").strip().lower()
            if choice == 'y':
                game.reset_game()
                continue
            else:
                print("\n感谢游戏！再见！")
                break

        # 显示当前玩家
        player_name = "黑棋(X)" if game.current_player == 'X' else "白棋(O)"
        print(f"当前玩家：{player_name}")

        # 获取用户输入
        user_input = input("请输入位置（行 列）或命令：").strip().lower()

        # 处理特殊命令
        if user_input in ['quit', 'q']:
            print("\n感谢游戏！再见！")
            break
        elif user_input in ['restart', 'r']:
            game.reset_game()
            print("\n游戏已重新开始！")
            continue
        elif user_input in ['undo', 'u']:
            if game.undo_move():
                print("\n已撤销上一步！")
            else:
                print("\n没有可撤销的步数！")
            continue

        # 解析坐标输入
        try:
            parts = user_input.split()
            if len(parts) != 2:
                print("输入格式错误！请输入：行号 列号")
                continue

            row = int(parts[0])
            col = int(parts[1])

            if game.make_move(row, col):
                print(f"\n落子成功：({row}, {col})")
            else:
                print("\n无效的移动！请检查：")
                print("1. 坐标是否在棋盘范围内")
                print("2. 该位置是否已有棋子")
        except ValueError:
            print("输入格式错误！请输入有效的数字。")
        except Exception as e:
            print(f"发生错误：{e}")


if __name__ == "__main__":
    main()
