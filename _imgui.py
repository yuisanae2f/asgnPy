import imgui
from imgui.integrations.glfw import GlfwRenderer
import glfw
import iobase

class IOImGUI(iobase.IOBase):
    def Puts(self, prompt: str) -> None:
        # Initialize GLFW
        if not glfw.init():
            return

        window = glfw.create_window(1280, 720, "ImGUI", None, None)
        glfw.make_context_current(window)
        imgui.create_context()
        renderer = GlfwRenderer(window)

        while not glfw.window_should_close(window):
            glfw.poll_events()
            imgui.new_frame()

            imgui.begin("Output:")
            imgui.text(prompt)
            imgui.end()

            imgui.render()
            renderer.render(imgui.get_draw_data())
            glfw.swap_buffers(window)

        renderer.shutdown()
        glfw.terminate()

    def Gets(self, prompt: str) -> str:
        return input(prompt)
    pass


import imgui
from imgui.integrations.glfw import GlfwRenderer
import glfw
import ctypes

def main():
    # GLFW 초기화
    if not glfw.init():
        return

    window = glfw.create_window(1280, 720, "Text Input Example", None, None)
    glfw.make_context_current(window)
    imgui.create_context()
    renderer = GlfwRenderer(window)

    # ctypes를 사용하여 수정 가능한 문자열 생성
    input_text = ctypes.create_string_buffer(256)  # 최대 256자까지 입력 가능

    while not glfw.window_should_close(window):
        glfw.poll_events()
        imgui.new_frame()

        imgui.begin("Text Input")
        imgui.input_text("Input Text", input_text.__str__(), 256)  # 텍스트 입력 필드 생성
        imgui.text(f"You entered: {input_text.value.decode('utf-8')}")  # 입력된 텍스트 표시
        imgui.end()

        imgui.render()
        renderer.render(imgui.get_draw_data())
        glfw.swap_buffers(window)

    renderer.shutdown()
    glfw.terminate()

if __name__ == "__main__":
    main()
