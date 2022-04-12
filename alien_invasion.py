import sys
import pygame
from settings import Settings
from ship import Ship

class AlienInvasion:
  def __init__(self):
    # ゲームを初期化し、ゲームのリソースを作成
      pygame.init()
      self.settings = Settings()
      self.screen = pygame.display.set_mode(
        (self.settings.screen_width,self.settings.screen_height))
      pygame.display.set_caption("エイリアン侵略")
      self.ship = Ship(self)
      #ゲームの背景色の設定
      self.bg_color = (230,230,230)
  def run_game(self):
    #ゲームのメインループの開始
    while True:
      for event in pygame.event.get():
        if event.type == pygame.QUIT:
          sys.exit()
      #ループを通過するたびに画面を再描画
      self.screen.fill(self.settings.bg_color)
      self.ship.blitme()
      #最新の状態の画面を表示
      pygame.display.flip()


if __name__ == '__main__':
  #ゲームのインスタンスを生成し、ゲームを実行
  ai = AlienInvasion()
  ai.run_game()