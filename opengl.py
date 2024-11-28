import pygame
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLU import *
import iobase

class IOGL(iobase.IOBase):
    def Gets(self, prompt: str) -> str:
        pygame.init()
        display = (800, 600)
        pygame.display.set_mode(display, DOUBLEBUF | OPENGL)
        gluPerspective(45, (display[0] / display[1]), 0.1, 50.0)
        glTranslatef(0.0, 0.0, -5)

        glClearColor(0, 0, 0, 1)  # 배경색을 검은색으로 설정
        input_text = ""
        clock = pygame.time.Clock()

        glEnable(GL_BLEND)
        glBlendFunc(GL_SRC_ALPHA, GL_ONE_MINUS_SRC_ALPHA)

        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    return
                if event.type == KEYDOWN:
                    if event.key == K_RETURN:  # Enter 키를 누르면
                        pygame.quit
                        return input_text
                    elif event.key == K_BACKSPACE:  # 백스페이스 키
                        input_text = input_text[:-1]  # 마지막 문자 삭제
                    else:
                        input_text += event.unicode  # 입력된 문자 추가

            glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
            
            # 텍스트 렌더링
            self.render_text(prompt, -0.9, 0.2)
            self.render_text(input_text, -0.9, 0)  # 사용자 지정 폰트 사용

            pygame.display.flip()
            clock.tick(60)

    def Puts(self, prompt: str) -> None:
        pygame.init()
        display = (800, 600)
        pygame.display.set_mode(display, DOUBLEBUF | OPENGL)
        gluPerspective(45, (display[0] / display[1]), 0.1, 50.0)
        glTranslatef(0.0, 0.0, -5)

        glClearColor(0, 0, 0, 1)  # 배경색을 검은색으로 설정
        input_text = prompt
        clock = pygame.time.Clock()

        glEnable(GL_BLEND)
        glBlendFunc(GL_SRC_ALPHA, GL_ONE_MINUS_SRC_ALPHA)

        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    return

            glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
            self.render_text(input_text, -0.9, 0) 

            pygame.display.flip()
            clock.tick(60)

    def render_text(self, text, x, y, font_size=36):
        font = pygame.font.Font(None, font_size)

        text_surface = font.render(text, True, (255, 255, 255))
        text_data = pygame.image.tostring(text_surface, "RGBA", True)
        
        width, height = text_surface.get_size()
        glRasterPos2f(x, y)
        glDrawPixels(width, height, GL_RGBA, GL_UNSIGNED_BYTE, text_data)

        pass
    pass

a = IOGL()
a.TestDeposit()
a.TestDiff()