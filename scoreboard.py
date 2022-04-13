from decimal import Rounded
from turtle import color
import pygame.font
class ScoreBoard:
  """得点の情報を表示する"""
  def __init__(self,ai_game):
    """得点を記録するための属性を初期化する"""
    self.screen = ai_game.screen
    self.screen_rect = self.screen.get_rect()
    self.settings = ai_game.settings
    self.stats = ai_game.stats

    #得点表示用のフォントを設定する
    self.text_color = (30,30,30)
    self.font = pygame.font.SysFont(None,48)

    #初期の得点画像を準備する
    self._prep_score()
    self.prep_high_score()

  def _prep_score(self):
    """得点を描画用の画像に変換する"""
    rounded_score = round(self.stats.score, -1)
    score_str = "{:,}".format(rounded_score)
    self.score_image = self.font.render(score_str,True,
              self.text_color,self.settings.bg_color)
    
    # 画面の右上に得点を表示する
    self.score_rect = self.score_image.get_rect()
    self.score_rect.right = self.screen_rect.right - 20
    self.score_rect.top = 20

  def prep_high_score(self):
    """ハイスコアを描画用の画像に変換する"""
    high_score = round(self.stats.high_score, -1)
    high_score_str = "{:,}".format(high_score)
    self.high_score_image = self.font.render(high_score_str,True,
            self.text_color, self.settings.bg_color)
    # 画面上部の中央にハイスコアを表示する
    self.high_score_rect = self.high_score_image.get_rect()
    self.high_score_rect.centerx = self.screen_rect.centerx
    self.high_score_rect.top = self.screen_rect.top

  def show_score(self):
    """画面に得点を描画する"""
    self.screen.blit(self.score_image,self.score_rect)
    self.screen.blit(self.high_score_image,self.high_score_rect)

  def check_high_score(self):
    """新しいハイスコアかをチェックし、必要であれば表示を更新する"""
    if self.stats.score > self.stats.high_score:
      self.stats.high_score = self.stats.score
      self.prep_high_score()
