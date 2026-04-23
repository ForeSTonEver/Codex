"""
파이썬 코딩 수행평가 - 오프라인 채점용 저지

문항 구성
1. 문항 1: 리스트 없이, 중첩 제어문 없이 해결하는 문제
2. 문항 2: 리스트와 중첩 제어문을 사용하는 문제
"""

from __future__ import annotations

import io
import sys
from dataclasses import dataclass
from typing import Dict, List, Tuple


@dataclass
class Problem:
    """문항 정보를 담는 데이터 클래스"""

    code: str
    title: str
    description: str
    input_desc: str
    output_desc: str
    examples: List[Tuple[str, str]]


class Judge:
    """온라인/오프라인 공용 채점 시스템"""

    def __init__(self):
        self.problems = self._create_problems()
        self.scores = {"1": 0, "2": 0}

    def _create_problems(self) -> Dict[str, Problem]:
        problems: Dict[str, Problem] = {}

        problems["1"] = Problem(
            code="1",
            title="세 과목 평균과 합격 판정",
            description="""
세 과목의 점수가 주어질 때 다음을 출력하는 프로그램을 작성하시오.

1. 세 과목의 총점
2. 세 과목의 평균 (소수점 첫째 자리까지 출력)
3. 합격 여부

[조건]
- 각 점수는 0 이상 100 이하의 정수이다.
- 평균이 60 이상이고, 세 과목 점수가 모두 40 이상이면 합격이다.
- 그렇지 않으면 불합격이다.
- 리스트를 사용하지 않는다.
- 중첩 제어문을 사용하지 않는다.
            """.strip(),
            input_desc="한 줄에 세 과목의 점수를 공백으로 구분하여 입력한다.",
            output_desc=(
                "첫째 줄에 총점을 출력한다.\n"
                "둘째 줄에 평균을 소수점 첫째 자리까지 출력한다.\n"
                "셋째 줄에 합격 또는 불합격을 출력한다."
            ),
            examples=[
                ("70 80 90", "240\n80.0\n합격"),
                ("100 35 90", "225\n75.0\n불합격"),
                ("40 40 40", "120\n40.0\n불합격"),
            ],
        )

        problems["2"] = Problem(
            code="2",
            title="점수 목록 분석과 등급 출력",
            description="""
학생 수와 점수 목록이 주어질 때 다음을 출력하는 프로그램을 작성하시오.

1. 평균 점수 (소수점 첫째 자리까지 출력)
2. 60점 이상인 학생 수
3. 입력된 순서대로 각 학생의 등급

[조건]
- 첫째 줄에 학생 수 n이 주어진다.
- 둘째 줄에 n개의 정수가 공백으로 구분되어 주어진다.
- 점수는 반드시 리스트에 저장하여 처리한다.
- 반복문 안에서 조건문을 사용하여 등급을 판정한다.
- 등급 기준은 다음과 같다.
  - 90 이상: A
  - 80 이상 90 미만: B
  - 70 이상 80 미만: C
  - 60 이상 70 미만: D
  - 60 미만: F
            """.strip(),
            input_desc=(
                "첫째 줄에 학생 수 n을 입력한다.\n"
                "둘째 줄에 n개의 점수를 공백으로 구분하여 입력한다."
            ),
            output_desc=(
                "첫째 줄에 평균 점수를 소수점 첫째 자리까지 출력한다.\n"
                "둘째 줄에 60점 이상인 학생 수를 출력한다.\n"
                "셋째 줄에 각 학생의 등급을 공백으로 구분하여 출력한다."
            ),
            examples=[
                ("5\n95 82 78 61 40", "71.2\n4\nA B C D F"),
                ("3\n100 100 100", "100.0\n3\nA A A"),
                ("4\n59 60 69 70", "64.5\n3\nF D D C"),
            ],
        )

        return problems

    def display_menu(self) -> None:
        print("\n" + "=" * 60)
        print("파이썬 코딩 수행평가 - 채점 프로그램")
        print("=" * 60)
        print("\n문항을 선택하세요:")
        print("1. 문항 1 - 세 과목 평균과 합격 판정")
        print("2. 문항 2 - 점수 목록 분석과 등급 출력")
        print("3. 종료")
        print("-" * 60)

    def display_problem(self, problem_code: str) -> None:
        problem = self.problems[problem_code]
        print("\n" + "=" * 60)
        print(f"[문항 {problem.code}] {problem.title}")
        print("=" * 60)
        print("\n【문제 설명】")
        print(problem.description)
        print("\n【입력 형식】")
        print(problem.input_desc)
        print("\n【출력 형식】")
        print(problem.output_desc)
        print("\n【입력/출력 예시】")

        for idx, (input_ex, output_ex) in enumerate(problem.examples, start=1):
            print(f"\n예시 {idx}")
            print(f"입력:\n{input_ex}")
            print(f"출력:\n{output_ex}")

    def get_user_solution(self) -> str:
        print("\n" + "-" * 60)
        print("【풀이 입력】")
        print("코드를 여러 줄로 입력한 뒤, 마지막 줄에 END를 입력하세요.")
        print("-" * 60)

        lines = []
        while True:
            line = input()
            if line.strip().upper() == "END":
                break
            lines.append(line)

        return "\n".join(lines)

    def test_solution(self, code: str, problem_code: str) -> Tuple[bool, str]:
        problem = self.problems[problem_code]

        try:
            compile(code, "<string>", "exec")
        except SyntaxError as exc:
            return False, f"문법 오류: {exc}"

        passed_tests = 0
        failed_test_info = None

        for idx, (input_ex, expected_output) in enumerate(problem.examples, start=1):
            old_stdin = sys.stdin
            old_stdout = sys.stdout

            try:
                sys.stdin = io.StringIO(input_ex)
                sys.stdout = io.StringIO()

                # 내장 함수 접근을 유지해 학생 코드 실행이 자연스럽게 동작하게 함
                exec(code, {"__builtins__": __builtins__})

                actual_output = sys.stdout.getvalue().strip()
                expected = expected_output.strip()
            except Exception as exc:
                return False, f"예시 {idx} 실행 오류: {exc}"
            finally:
                sys.stdout = old_stdout
                sys.stdin = old_stdin

            if actual_output == expected:
                passed_tests += 1
            elif failed_test_info is None:
                failed_test_info = (idx, input_ex, expected, actual_output)

        if passed_tests == len(problem.examples):
            return True, f"모든 테스트 케이스 통과! ({passed_tests}/{len(problem.examples)})"

        idx, input_ex, expected, actual = failed_test_info
        return (
            False,
            f"예시 {idx} 실패\n입력: {input_ex}\n기대 출력: {expected}\n실제 출력: {actual}",
        )

    def run(self) -> None:
        print("\n환영합니다! 파이썬 코딩 수행평가를 시작합니다.\n")

        while True:
            self.display_menu()
            choice = input("선택 (1-3): ").strip()

            if choice == "3":
                self._show_final_score()
                break

            if choice not in {"1", "2"}:
                print("잘못된 선택입니다. 다시 시도하세요.")
                continue

            self.display_problem(choice)
            user_code = self.get_user_solution()

            if not user_code.strip():
                print("\n입력된 코드가 없습니다.")
                continue

            print("\n" + "=" * 60)
            print("【채점 중...】")
            print("=" * 60)

            passed, message = self.test_solution(user_code, choice)

            if passed:
                self.scores[choice] = 100
                print(f"\n✓ 정답입니다!\n{message}")
                print("\n점수: 100점")
            else:
                print(f"\n✗ 오답입니다.\n{message}")
                print("\n점수: 0점")

            input("\n계속하려면 Enter 키를 누르세요...")

    def _show_final_score(self) -> None:
        total = sum(self.scores.values())
        print("\n" + "=" * 60)
        print("【최종 성적】")
        print("=" * 60)
        print(f"문항 1: {self.scores['1']:3d}점")
        print(f"문항 2: {self.scores['2']:3d}점")
        print("-" * 60)
        print(f"총점: {total}/200점")
        print("=" * 60)
        print("\n수고하셨습니다!")


def main() -> None:
    Judge().run()


if __name__ == "__main__":
    main()
