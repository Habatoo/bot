
class Config:
    with open(
        './data/chatbot.txt', 'r', encoding='utf-8', errors = 'ignore') as f:
        CORPUS = f.read()

if __name__ == '__main__':
    test_config = Config()
    print(test_config.CORPUS)
