class Solution2:  # first try, ~ 40 minutes
    separator = "2004"

    def encode(self, strs: List[str]) -> str:  # O(n)
        n_words = len(strs)
        separator = self.separator
        ret_str = f"{n_words}"
        for i in range(0, len(strs)):
            ret_str += separator + strs[i]

        return ret_str

    def decode(self, s: str) -> List[str]:  # O(n)
        separator = self.separator
        ret_list = []
        buf = ""

        wc_flag = 0
        i = 0

        while i < len(s):
            if wc_flag == 1:
                n_words = int(ret_list[0])
                if n_words == 0:
                    return []
            if s[i : i + len(separator)] == separator:
                print(buf)
                ret_list.append(buf)
                buf = ""
                wc_flag += 1
                i += len(separator)
            else:
                buf += s[i]
                i += 1

        ret_list.append(buf)

        return ret_list[1:]


# second try, with hints:
class Solution:  # first try, ~ 40 minutes
    separator = "Z"

    def encode(self, strs: List[str]) -> str:  # O(n)
        sep = self.separator
        if len(strs) == 0:
            return f"00"  # edge case

        ret_str = ""
        for w in strs:
            ret_str += f"{len(w)}{sep}" + w

        print(ret_str)

        return ret_str

    def decode(self, s: str) -> List[str]:  # O(n)
        i = 0
        w_len = -1
        sep = self.separator
        sep_len = len(sep)

        if s == "00":
            return []

        ret_l = []
        buf = ""
        while i < len(
            s
        ):  # 3Z 123 3Z 456 3Z7892Z102Z112Z122Z132Z142Z152Z162Z172Z182Z192Z20
            if s[i : i + sep_len] == sep:
                w_len = int(buf)
                buf = ""

                ret_l.append(s[i + sep_len : i + sep_len + w_len])
                i += w_len + sep_len
            else:
                buf += s[i]
                i += 1

        return ret_l


print(
    Solution.decode(
        Solution,
        Solution.encode(
            Solution,
            strs=[
                "123",
                "456",
                "789",
                "10",
                "11",
                "12",
                "13",
                "14",
                "15",
                "16",
                "17",
                "18",
                "19",
                "20",
            ],
        ),
    )
)
