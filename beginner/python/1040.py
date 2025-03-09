N1, N2, N3, N4 = map(float, input().split())

avg = ((N1 * 2) + (N2 * 3) + (N3 * 4) + (N4 * 1)) / 10

print(f"Media: {avg:.1f}")

if avg >= 7.0:
    print("Aluno aprovado.")
elif avg < 5.0:
    print("Aluno reprovado.")
else:
    print("Aluno em exame.")
    exam = float(input())
    print(f"Nota do exame: {exam:.1f}")

    final_avg = (avg + exam) / 2

    if final_avg >= 5.0:
        print("Aluno aprovado.")
    else:
        print("Aluno reprovado.")

    print(f"Media final: {final_avg:.1f}")
