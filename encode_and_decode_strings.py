class Solution:

    def encode(self, strs: List[str]) -> str:
        st=""
        for x in strs:
            st=st+str(len(x))+"#"+x
        return st

    def decode(self, s: str) -> List[str]:
        output=[]
        i=0
        
        while i < len(s):
            j=i
            w_ln=""
            while s[j]!="#":
                w_ln+=s[j]
                j+=1

            word_len=int(w_ln)
            start=j+1
            end=start+word_len
            output.append(s[start:end])

            i=end

        return output

    # Encode
    # Time Complexity: O(n)
    #   n = total number of characters across all strings
    #   We build one output string by visiting each character once.
    # Space Complexity: O(n)
    #   The encoded result stores all input characters plus length markers.

    # Decode
    # Time Complexity: O(n)
    #   n = length of the encoded string
    #   We scan each character once to parse lengths and slice substrings.
    # Space Complexity: O(n)
    #   The output list holds all original strings whose total size is O(n).

        




