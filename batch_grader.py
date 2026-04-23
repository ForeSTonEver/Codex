#!/usr/bin/env python3
"""
오프라인 제출 폴더 일괄 채점 스크립트

사용 예시:
    python3 batch_grader.py --problem 1 --submissions-dir submissions/problem1
    python3 batch_grader.py --problem 2 --submissions-dir submissions/problem2 --output reports/problem2.csv
"""

from __future__ import annotations

import argparse
import csv
from dataclasses import dataclass
from datetime import datetime
from pathlib import Path
from typing import List

from judge import Judge


@dataclass
class GradeResult:
    filename: str
    student_name: str
    score: int
    passed: bool
    message: str


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="제출 폴더에 모인 파이썬 파일을 오프라인으로 일괄 채점합니다."
    )
    parser.add_argument(
        "--problem",
        required=True,
        choices=["1", "2"],
        help="채점할 문항 번호",
    )
    parser.add_argument(
        "--submissions-dir",
        required=True,
        help="학생 제출 파일(.py)이 모여 있는 폴더 경로",
    )
    parser.add_argument(
        "--output",
        help="채점 결과 CSV 파일 경로. 생략하면 reports 폴더에 자동 생성합니다.",
    )
    return parser.parse_args()


def load_code(file_path: Path) -> str:
    return file_path.read_text(encoding="utf-8")


def grade_submission(judge: Judge, problem_code: str, file_path: Path) -> GradeResult:
    try:
        code = load_code(file_path)
    except UnicodeDecodeError:
        return GradeResult(
            filename=file_path.name,
            student_name=file_path.stem,
            score=0,
            passed=False,
            message="파일 인코딩 오류: UTF-8로 읽을 수 없습니다.",
        )
    except OSError as exc:
        return GradeResult(
            filename=file_path.name,
            student_name=file_path.stem,
            score=0,
            passed=False,
            message=f"파일 읽기 오류: {exc}",
        )

    if not code.strip():
        return GradeResult(
            filename=file_path.name,
            student_name=file_path.stem,
            score=0,
            passed=False,
            message="빈 파일입니다.",
        )

    passed, message = judge.test_solution(code, problem_code)
    return GradeResult(
        filename=file_path.name,
        student_name=file_path.stem,
        score=100 if passed else 0,
        passed=passed,
        message=message,
    )


def ensure_output_path(output_arg: str | None, problem_code: str) -> Path:
    if output_arg:
        output_path = Path(output_arg)
    else:
        reports_dir = Path("reports")
        reports_dir.mkdir(exist_ok=True)
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        output_path = reports_dir / f"grade_problem_{problem_code}_{timestamp}.csv"

    output_path.parent.mkdir(parents=True, exist_ok=True)
    return output_path


def write_csv(results: List[GradeResult], output_path: Path) -> None:
    with output_path.open("w", newline="", encoding="utf-8-sig") as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(["파일명", "학생", "점수", "정답 여부", "결과 메시지"])
        for result in results:
            writer.writerow(
                [
                    result.filename,
                    result.student_name,
                    result.score,
                    "정답" if result.passed else "오답",
                    result.message,
                ]
            )


def print_summary(results: List[GradeResult], problem_code: str, output_path: Path) -> None:
    print("\n" + "=" * 72)
    print(f"【오프라인 일괄 채점 결과】 - 문항: {problem_code}")
    print("=" * 72)

    if not results:
        print("채점할 .py 파일이 없습니다.")
        print("=" * 72)
        return

    header = f"{'학생':20} {'파일명':28} {'점수':>4}  결과"
    print(header)
    print("-" * 72)

    for result in results:
        status = "정답" if result.passed else "오답"
        print(f"{result.student_name[:20]:20} {result.filename[:28]:28} {result.score:>4}  {status}")

    passed_count = sum(1 for result in results if result.passed)
    total = len(results)
    average = sum(result.score for result in results) / total if total else 0

    print("-" * 72)
    print(f"총 제출 수: {total}명")
    print(f"정답 수: {passed_count}명")
    print(f"평균 점수: {average:.1f}점")
    print(f"CSV 저장: {output_path}")
    print("=" * 72)


def main() -> None:
    args = parse_args()
    submissions_dir = Path(args.submissions_dir)

    if not submissions_dir.exists():
        raise SystemExit(f"제출 폴더가 존재하지 않습니다: {submissions_dir}")
    if not submissions_dir.is_dir():
        raise SystemExit(f"제출 경로가 폴더가 아닙니다: {submissions_dir}")

    judge = Judge()
    output_path = ensure_output_path(args.output, args.problem)
    submission_files = sorted(submissions_dir.glob("*.py"))

    results = [
        grade_submission(judge, args.problem, file_path)
        for file_path in submission_files
    ]

    write_csv(results, output_path)
    print_summary(results, args.problem, output_path)


if __name__ == "__main__":
    main()
