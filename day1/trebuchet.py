
class TrebuchetDecoder:

    def __init__(self, file_name: str) -> None:
        self.file_name = file_name

    def get_calibration_values(self) -> int:
        sum = 0

        with open(self.file_name) as file:
            for line in file.readlines():
                digits = []

                i = 0
                while i < len(line):
                    if line[i].isdigit():
                        digits.append(line[i])
                    for d, val in enumerate(["one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]):
                        if line[i:].startswith(val):
                            digits.append(str(d+1))

                    i += 1
                decode = digits[0] + digits[-1]
                
                sum += int(decode)

        return sum
    
if __name__ == "__main__":
    decoder = TrebuchetDecoder("trebuchetInput.txt")
    print(decoder.get_calibration_values())