import pulp as plp


model = plp.LpProblem("Napoyi Company", plp.LpMaximize)
# лимонад
L = plp.LpVariable("L", 0, None, cat="Integer")
# фруктовий сік
S = plp.LpVariable("S", 0, None, cat="Integer")

# цільова функція
model += L + S, "Profit"

# обмеження
# сумарне обмеження щодо води
model += 2 * L + 1 * S <= 100, "Voda"
# обмеження виробництва лимонаду щодо води
model += L <= 100 / 2, "Voda_L"
# обмеження виробництва лимонаду щодо цукру
model += L <= 50, "Tsukor"
# обмеження виробництва лимонаду щодо лимонного соку
model += L <= 30, "Lymonnyi_sik"
# обмеження виробництва фруктового соку щодо води
model += S <= 100, "Voda_S"
# обмеження виробництва фруктового соку щодо фруктового пюре
model += S <= 40 / 2, "Fructove_pure"

model.solve()
print(f"Status: {plp.LpStatus[model.status]}")
print(f"Лимонаду потрібно виробляти: {plp.value(L)}")
print(f"Фруктового соку потрібно виробляти: {plp.value(S)}")
print(f"Сумарна максимальна кількість виробів = {plp.value(model.objective)}")
