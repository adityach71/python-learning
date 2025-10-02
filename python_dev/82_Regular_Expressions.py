import re

pattern =r"[A-Z]+yclone"
text = '''1975)text = "CYclone is a word. Another CYCLONE is here." was the manager of the championship New York Yankees baseball teams of the 1950s and of the New York Mets of the early 1960s. An outfielder for the 1912 Brooklyn Dodgers, he played on their 1916 National League-winning team, then for the Philadelphia Phillies, the New York Giants and the Boston Braves. In 1925, he began a career as a manager, with mostly poor finishes for the next 20 years. In 1948, after he won the PCL title with the Oakland Oaks, the Yankees hired him. In his twelve seasons, they won ten pennants and seven World Series, including a record-setting five in a row (1949–1953), but Stengel was fired after losing the 1960 World Series. The Mets were an expansion team when they hired him in late 1961. They finished last all four seasons with Stengel, and he retired in 1965. Remembered as one of the great characters in baseball history, and known for his humorous sayings, Stengel was elected to the Baseball Hall of Fame in 1966. (Full article...'''

matches = re.finditer(pattern, text)
for match in matches:
    print(match.span())
    print(text[match.span()[0]:match.span()[1]])
