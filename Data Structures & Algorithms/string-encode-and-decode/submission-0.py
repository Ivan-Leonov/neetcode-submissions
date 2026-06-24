class Solution:

    def encode(self, strs: List[str]) -> str:
        return "".join(map(
            lambda x: str(len(x)).zfill(3) + x,
            strs
        ))

        
    def decode(self, s: str) -> List[str]:
        strs = []
        i = 0
        while i < len(s):
            sl = int(s[i:i+3])
            strs.append(s[i+3:i+3+sl])
            i += 3 + sl
        return strs
