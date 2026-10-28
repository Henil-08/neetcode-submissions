class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded_string = '__i__'.join(strs) if len(strs) > 0 else 'None'

        return encoded_string
            
    def decode(self, s: str) -> List[str]:
        decoded_string = s.split('__i__') if s!='None' else []
        
        return decoded_string
