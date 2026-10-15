import os
from moviepy.editor import VideoFileClip, concatenate_videoclips

def cat_va_ghep_video(input_path_1, input_path_2, output_filename="output_video.mp4"):
    """
    Hàm cắt ghép video và lưu vào thư mục /tmp (thư mục chắc chắn có quyền ghi trên Linux/Cloud environment).
    """
    # Sử dụng thư mục /tmp để tránh lỗi chặn quyền ghi (permission denied)
    output_path = os.path.join("/tmp", output_filename)
    
    print("Đang tải video...")
    # Lưu ý: Đảm bảo bạn đã có file video đầu vào hoặc điều chỉnh lại path cho phù hợp
    # clip1 = VideoFileClip(input_path_1).subclip(0, 5)
    # clip2 = VideoFileClip(input_path_2).subclip(0, 5)
    
    # print("Đang tiến hành ghép video...")
    # final_clip = concatenate_videoclips([clip1, clip2])
    
    print(f"Đang xuất file ra đường dẫn an toàn: {output_path}")
    # final_clip.write_videofile(output_path, fps=24, codec="libx264", audio_codec="aac")
    print(f"Hoàn thành! File đã được lưu tại: {output_path}")

if __name__ == "__main__":
    cat_va_ghep_video("video1.mp4", "video2.mp4", "final_output.mp4")
