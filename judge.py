"""
파이썬 코딩 수행평가 - 온라인 저지 (Online Judge)
난이도: 상, 중, 하 각 1문제
포함요소: 변수, 자료형, 선택구조, 반복구조, 리스트
"""

import sys
import io
from typing import Tuple, List, Any


class Problem:
    """문제를 담는 클래스"""
    def __init__(self, title: str, description: str, input_desc: str, 
                 output_desc: str, examples: List[Tuple[str, str]]):
        self.title = title
        self.description = description
        self.input_desc = input_desc
        self.output_desc = output_desc
        self.examples = examples  # [(입력, 출력), ...]


class Judge:
    """온라인 저지 시스템"""
    
    def __init__(self):
        self.problems = self._create_problems()
        self.scores = {"상": 0, "중": 0, "하": 0}
    
    def _create_problems(self) -> dict:
        """문제 생성"""
        problems = {}
        
        # ============ 하(쉬움) 문제 ============
        problems["하"] = Problem(
            title="리스트에서 최댓값과 최솟값 찾기",
            description="""
정수 리스트가 주어질 때, 다음을 구하는 프로그램을 작성하시오.
1. 리스트의 최댓값
2. 리스트의 최솟값
3. 두 값의 합

[포함 요소]
- 변수: n, numbers, max_val, min_val, sum_val
- 자료형: int, list
- 반복구조: for문으로 리스트 순회
- 선택구조: if문으로 최댓값/최솟값 비교
            """,
            input_desc="첫 번째 줄: 정수 개수 n (1 ≤ n ≤ 100)\n두 번째 줄: n개의 정수 (공백으로 구분)",
            output_desc="첫 번째 줄: 최댓값\n두 번째 줄: 최솟값\n세 번째 줄: 두 값의 합",
            examples=[
                ("5\n10 20 5 30 15", "30\n5\n35"),
                ("3\n-5 0 10", "10\n-5\n5"),
                ("1\n42", "42\n42\n84")
            ]
        )
        
        # ============ 중(중간) 문제 ============
        problems["중"] = Problem(
            title="학점 계산 및 성적 순위",
            description="""
학생들의 점수가 주어질 때, 다음을 구하는 프로그램을 작성하시오.
1. 각 학생의 학점 계산 (90~: A, 80~: B, 70~: C, 60~: D, ~59: F)
2. A학점의 개수 세기
3. 평균 점수 계산
4. 점수 리스트를 내림차순으로 정렬하여 출력

[포함 요소]
- 변수: scores, grades, count_a, average, sorted_scores
- 자료형: int, str, list, float
- 반복구조: for문으로 점수별 학점 부여 및 계산
- 선택구조: if/elif/else로 학점 판정
            """,
            input_desc="첫 번째 줄: 학생 수 n\n다음 n줄: 각 학생의 점수 (0~100)",
            output_desc="첫 번째 줄: A학점 개수\n두 번째 줄: 평균 점수 (소수점 1자리)\n세 번째 줄: 내림차순 정렬 점수 (공백으로 구분)",
            examples=[
                ("5\n95\n82\n78\n91\n65", "2\n82.2\n95 91 82 78 65"),
                ("3\n100\n50\n75", "1\n75.0\n100 75 50"),
                ("4\n88\n92\n85\n90", "2\n88.8\n92 90 88 85")
            ]
        )
        
        # ============ 상(어려움) 문제 ============
        problems["상"] = Problem(
            title="소수 판별 및 필터링",
            description="""
정수 리스트가 주어질 때, 다음을 구하는 프로그램을 작성하시오.
1. 리스트에서 소수만 필터링
2. 필터링된 소수의 개수
3. 소수들의 합
4. 소수 여부를 True/False 리스트로 표현

소수: 1보다 큰 자연수 중 1과 자기자신으로만 나누어떨어지는 수

[포함 요소]
- 변수: numbers, primes, count, sum_primes, is_prime_list
- 자료형: int, bool, list
- 반복구조: 이중 for문 (소수 판별)
- 선택구조: if문 (소수 판별 로직)
            """,
            input_desc="첫 번째 줄: 정수 개수 n\n두 번째 줄: n개의 정수 (공백으로 구분)",
            output_desc="첫 번째 줄: 소수 개수\n두 번째 줄: 소수들의 합\n세 번째 줄: 각 수별 소수 여부 (True/False, 공백으로 구분)",
            examples=[
                ("6\n2 3 4 5 6 7", "4\n17\nTrue True False True False True"),
                ("5\n1 10 11 12 13", "2\n24\nFalse False True False True"),
                ("4\n97 98 99 100", "1\n97\nTrue False False False")
            ]
        )
        
        return problems
    
    def display_menu(self):
        """메인 메뉴 표시"""
        print("\n" + "="*60)
        print("파이썬 코딩 수행평가 - 온라인 저지 (Online Judge)")
        print("="*60)
        print("\n난이도를 선택하세요:")
        print("1. 하 (쉬움) - 리스트 최댓값/최솟값 찾기")
        print("2. 중 (중간) - 학점 계산 및 성적 순위")
        print("3. 상 (어려움) - 소수 판별 및 필터링")
        print("4. 종료")
        print("-"*60)
    
    def display_problem(self, difficulty: str):
        """문제 표시"""
        problem = self.problems[difficulty]
        print("\n" + "="*60)
        print(f"[{difficulty}] {problem.title}")
        print("="*60)
        print("\n【문제설명】")
        print(problem.description)
        print("\n【입력 형식】")
        print(problem.input_desc)
        print("\n【출력 형식】")
        print(problem.output_desc)
        print("\n【입력/출력 예시】")
        for idx, (input_ex, output_ex) in enumerate(problem.examples, 1):
            print(f"\n예시 {idx}:")
            print(f"입력:\n{input_ex}")
            print(f"출력:\n{output_ex}")
    
    def get_user_solution(self) -> str:
        """사용자의 코드 입력받기"""
        print("\n" + "-"*60)
        print("【풀이 입력】")
        print("코드를 입력하세요 (여러 줄 가능, 'END'를 입력하여 종료):")
        print("-"*60)
        
        lines = []
        while True:
            line = input()
            if line.strip().upper() == "END":
                break
            lines.append(line)
        
        return "\n".join(lines)
    
    def test_solution(self, code: str, difficulty: str) -> Tuple[bool, str]:
        """사용자의 풀이 검증"""
        import io
        problem = self.problems[difficulty]
        
        # 문법 검사
        try:
            compile(code, '<string>', 'exec')
        except SyntaxError as e:
            return False, f"문법 오류: {str(e)}"
        
        # 모든 예시에 대해 테스트
        passed_tests = 0
        failed_test_info = None
        
        for idx, (input_ex, expected_output) in enumerate(problem.examples, 1):
            try:
                # 입력/출력 시뮬레이션
                old_stdin = sys.stdin
                old_stdout = sys.stdout
                
                sys.stdin = io.StringIO(input_ex)
                sys.stdout = io.StringIO()
                
                # 사용자 코드 실행
                exec(code, {})
                
                # 출력 가져오기
                actual_output = sys.stdout.getvalue().strip()
                expected = expected_output.strip()
                
                # 복원
                sys.stdout = old_stdout
                sys.stdin = old_stdin
                
                # 비교
                if actual_output == expected:
                    passed_tests += 1
                else:
                    if failed_test_info is None:
                        failed_test_info = (idx, input_ex, expected, actual_output)
            
            except Exception as e:
                sys.stdout = old_stdout
                sys.stdin = old_stdin
                return False, f"예시 {idx} 실행 오류: {str(e)}"
        
        # 결과 판정
        if passed_tests == len(problem.examples):
            return True, f"모든 테스트 케이스 통과! ({passed_tests}/{len(problem.examples)})"
        else:
            idx, input_ex, expected, actual = failed_test_info
            return False, f"예시 {idx} 실패\n입력: {input_ex}\n기대 출력: {expected}\n실제 출력: {actual}"
    
    def run(self):
        """프로그램 실행"""
        print("\n환영합니다! 파이썬 코딩 수행평가를 시작합니다.\n")
        
        while True:
            self.display_menu()
            choice = input("선택 (1-4): ").strip()
            
            if choice == "4":
                self._show_final_score()
                break
            elif choice in ["1", "2", "3"]:
                difficulty_map = {"1": "하", "2": "중", "3": "상"}
                difficulty = difficulty_map[choice]
                
                self.display_problem(difficulty)
                
                # 풀이 입력
                user_code = self.get_user_solution()
                
                if not user_code.strip():
                    print("\n입력된 코드가 없습니다.")
                    continue
                
                # 테스트
                print("\n" + "="*60)
                print("【채점 중...】")
                print("="*60)
                
                passed, message = self.test_solution(user_code, difficulty)
                
                if passed:
                    print(f"\n✓ 정답입니다!\n{message}")
                    self.scores[difficulty] = 100
                    print(f"\n점수: 100점 획득")
                else:
                    print(f"\n✗ 오답입니다.\n{message}")
                    print(f"\n점수: 0점")
                
                input("\n계속하려면 Enter 키를 누르세요...")
            else:
                print("잘못된 선택입니다. 다시 시도하세요.")
    
    def _show_final_score(self):
        """최종 성적 표시"""
        total = sum(self.scores.values())
        print("\n" + "="*60)
        print("【최종 성적】")
        print("="*60)
        print(f"하 (쉬움): {self.scores['하']:3d}점")
        print(f"중 (중간): {self.scores['중']:3d}점")
        print(f"상 (어려움): {self.scores['상']:3d}점")
        print("-"*60)
        print(f"총점: {total}/300점")
        print("="*60)
        print("\n수고하셨습니다!")


def main():
    judge = Judge()
    judge.run()


if __name__ == "__main__":
    main()
