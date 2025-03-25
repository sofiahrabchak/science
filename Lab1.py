import csv
from typing import List, Dict

class Block:
    def __init__(self, block_id: str, view: int):
        self.id = block_id
        self.view = view
    
    def __repr__(self):
        return f"Block(id={self.id}, view={self.view})"

class Blockchain:
    def __init__(self):
        self.chain = []
        self.votes = set()
    
    def add_vote(self, block_id: str):
        self.votes.add(block_id)
    
    def add_block(self, block: Block):
        if block.id in self.votes and (not self.chain or self.chain[-1].view == block.view - 1):
            self.chain.append(block)
    
    def __repr__(self):
        return f"Blockchain(chain={self.chain})"

def read_blocks_from_csv(filename: str = "blocks_votes.csv") -> List[Block]:
    blocks = []
    with open(filename, newline='', encoding='utf-8') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            if row['id'] and row['view']:  
                try:
                    blocks.append(Block(row['id'], int(row['view'])))
                except ValueError:
                    print(f"Помилка у файлі CSV: неправильне значення view у рядку {row}")
    return blocks

def read_votes_from_csv(filename: str = "blocks_votes.csv") -> List[str]:
    votes = []
    with open(filename, newline='', encoding='utf-8') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            if 'block_id' in row and row['block_id']:  
                votes.append(row['block_id'])
    return votes

def main():
    print("Програма запущена! Обробка даних...")
    blockchain = Blockchain()
    
    blocks = read_blocks_from_csv()
    votes = read_votes_from_csv()
    
    for vote in votes:
        blockchain.add_vote(vote)
    
    for block in sorted(blocks, key=lambda b: b.view):  
        blockchain.add_block(block)
    
    print("Фінальний ланцюг блоків:")
    for block in blockchain.chain:
        print(block)

if __name__ == "__main__":
    main()
