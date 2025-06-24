
import requests
import time
from urllib.parse import urlparse

def download_speed_test(url, test_times=5):
    """
    测试从指定URL下载文件的速度和流量消耗
    :param url: 测试URL
    :param test_times: 测试次数
    :return: 平均下载速度(MB/s)和总流量消耗(MB)
    """
    total_size = 0
    total_time = 0
    
    try:
        # 检查URL是否有效
        response = requests.head(url)
        if response.status_code != 200:
            print(f"错误：无法访问URL，状态码 {response.status_code}")
            return None, None
        
        for i in range(test_times):
            print(f"正在进行第 {i+1} 次测试...")
            start_time = time.time()
            response = requests.get(url, stream=True)
            response.raise_for_status()
            
            # 获取文件大小
            file_size = int(response.headers.get('content-length', 0))
            if file_size == 0:
                print("警告：无法获取文件大小，可能影响速度计算准确性")
            
            # 下载文件
            downloaded = 0
            for chunk in response.iter_content(chunk_size=8192):
                downloaded += len(chunk)
            
            end_time = time.time()
            duration = end_time - start_time
            speed = (file_size / (1024 * 1024)) / duration  # MB/s
            
            total_size += file_size
            total_time += duration
            
            print(f"第 {i+1} 次测试结果: 速度 {speed:.2f} MB/s, 耗时 {duration:.2f} 秒")
        
        avg_speed = (total_size / (1024 * 1024)) / total_time
        total_consumed = total_size / (1024 * 1024)
        
        print(f"\n测试完成，共测试 {test_times} 次")
        print(f"平均下载速度: {avg_speed:.2f} MB/s")
        print(f"总流量消耗: {total_consumed:.2f} MB")
        
        return avg_speed, total_consumed
    
    except Exception as e:
        print(f"测试过程中发生错误: {str(e)}")
        return None, None

if __name__ == "__main__":
    test_url = "https://dnuootg.zjxaq.com/yzs3tjoun2.apk"
    test_count = 100
    download_speed_test(test_url, test_count)
