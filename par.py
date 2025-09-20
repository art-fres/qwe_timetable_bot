import requests # type: ignore
import time
from bs4 import BeautifulSoup # type: ignore
import random
import re
import urllib.parse
from crypto import encoded_string
#-----------------------------------------------------------

def get_enhanced_headers():
    """Генерирует улучшенные заголовки для обхода защиты"""
    user_agents = [
        'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
        'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:121.0) Gecko/20100101 Firefox/121.0',
        'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/17.1 Safari/605.1.15',
        'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36'
    ]
    
    return {
        'User-Agent': random.choice(user_agents),
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8',
        'Accept-Language': 'ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7',
        'Accept-Encoding': 'gzip, deflate, br',
        'Connection': 'keep-alive',
        'Upgrade-Insecure-Requests': '1',
        'Sec-Fetch-Dest': 'document',
        'Sec-Fetch-Mode': 'navigate',
        'Sec-Fetch-Site': 'none',
        'Sec-Fetch-User': '?1',
        'Cache-Control': 'max-age=0',
        'Referer': 'https://yandex.ru/',
        'DNT': '1',
        'sec-ch-ua': '"Not_A Brand";v="8", "Chromium";v="120", "Google Chrome";v="120"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
    }

def simulate_human_behavior():
    """Имитирует человеческое поведение"""
    # Случайные задержки между действиями
    time.sleep(random.uniform(3, 8))
    # Случайные движения мыши (имитация)
    if random.random() > 0.7:
        time.sleep(random.uniform(0.5, 1.5))

def make_stealth_request(url, max_retries=3):
    """Выполняет скрытный запрос с повторными попытками"""
    for attempt in range(max_retries):
        simulate_human_behavior()
        
        headers = get_enhanced_headers()
        cookies = {'yandexuid': str(random.randint(1000000000, 9999999999))}
        
        try:
            # Добавляем случайные параметры к URL
            if '?' in url:
                modified_url = f"{url}&_={int(time.time())}{random.randint(100,999)}"
            else:
                modified_url = f"{url}?_{int(time.time())}{random.randint(100,999)}"
            
            response = requests.get(
                modified_url,
                headers=headers,
                cookies=cookies,
                timeout=15,
                allow_redirects=True,
                verify=True
            )
            
            
            
            if response.status_code == 200:
                return response
            elif response.status_code == 403:
                print("Обнаружена защита 403, жду...")
                time.sleep(random.uniform(10, 20))
            else:
                time.sleep(random.uniform(5, 10))
                
        except Exception as e:
            print(f"Ошибка при попытке {attempt + 1}: {e}")
            time.sleep(random.uniform(8, 15))
    
    return None

#-----------------------------------------------------------

def extract_links_from_text(text):
    """Извлекает ссылки из текста (если не удалось получить через запрос)"""
    patterns = [
        r'https?://downloader\.disk\.yandex\.ru/preview/[a-f0-9]+/[a-f0-9]+/[^\s"\']*?\?[^\s"\']*',
        r'https?://[^\s"\']*?\.yandex\.[^\s"\']*?/disk/[^\s"\']*',
        r'https?://[^\s"\']*?\.yandex\.[^\s"\']*?/preview/[^\s"\']*',
    ]
    
    links = []
    for pattern in patterns:
        found = re.findall(pattern, text, re.IGNORECASE)
        links.extend(found)
    
    return list(set(links))

#-----------------------------------------------------------

def f(url):
    return url.replace('\\u0026', '&')





# Основной код
url = 'https://disk.yandex.ru/d/XxomzufLFsEapQ'



response = make_stealth_request(url)

if response and response.status_code == 200:
    
    
    # Анализ содержимого
    links = extract_links_from_text(response.text)

    # Исправляем только проблему с \u0026
    fixed_links = []
    for link in links:
        fixed_link = f(link)
        fixed_links.append(fixed_link)

    
    
    filtered_links = []
    for i, link in enumerate(fixed_links, 1):
        if "size=XXXL" in link:
            # print(f"{i}. {link}")
            filtered_links.append(link)
    
    filtered_links.sort(key=len)
    
    
    # # Сохранение результатов
    # with open('yandex_links.txt', 'w', encoding='utf-8') as f:
    #     f.write(f"Ссылки из: {url}\n")
    #     f.write(f"Время: {time.strftime('%Y-%m-%d %H:%M:%S')}\n")
    #     f.write(f"Найдено ссылок: {len(fixed_links)}\n")
    #     f.write(f"Отфильтровано ссылок: {len(filtered_links)}\n\n")
        
    #     for link in filtered_links:
    #         f.write(f"{link}\n\n")
    
    # print(f"\n💾 Результаты сохранены в yandex_links.txt")