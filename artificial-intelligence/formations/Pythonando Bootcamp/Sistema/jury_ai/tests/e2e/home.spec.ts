import { test, expect } from "@playwright/test";

test.describe("Páginas principais", () => {
  test("página inicial carrega e exibe título", async ({ page }) => {
    await page.goto("/");
    await expect(page).toHaveTitle(/Juri\.AI/i);
    await expect(page.getByRole("heading", { name: /entre em sua conta/i })).toBeVisible();
  });

  test("página de login carrega", async ({ page }) => {
    await page.goto("/login/");
    await expect(page.getByRole("heading", { name: /entrar|login/i })).toBeVisible();
    await expect(page.getByLabel(/username|usuário/i)).toBeVisible();
  });

  test("página de cadastro carrega", async ({ page }) => {
    await page.goto("/cadastro/");
    await expect(page.getByRole("heading", { name: /crie sua conta/i })).toBeVisible();
  });
});
