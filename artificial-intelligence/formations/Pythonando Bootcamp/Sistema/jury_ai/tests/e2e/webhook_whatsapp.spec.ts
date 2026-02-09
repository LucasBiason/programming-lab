import { test, expect } from "@playwright/test";

test.describe("Webhook WhatsApp (Evolution API)", () => {
  test("GET /api/whatsapp/webhook/ retorna status ok", async ({ request }) => {
    const res = await request.get("/api/whatsapp/webhook/");
    expect(res.ok()).toBeTruthy();
    const data = await res.json();
    expect(data.status).toBe("ok");
    expect(data.webhook).toBe("jury_ai");
  });

  test("POST /api/whatsapp/webhook/ com payload válido retorna 200", async ({
    request,
  }) => {
    const payload = {
      event: "messages.upsert",
      instance: "default",
      data: {
        key: {
          remoteJid: "5516992805441@s.whatsapp.net",
          fromMe: false,
          id: "test-id",
        },
        pushName: "xptd",
        message: {
          extendedTextMessage: { text: "Qual o meu nome?" },
        },
      },
    };
    const res = await request.post("/api/whatsapp/webhook/", {
      data: payload,
      headers: { "Content-Type": "application/json" },
    });
    expect(res.status()).toBe(200);
    const data = await res.json();
    expect(data.received).toBe(true);
  });

  test("GET /api/whatsapp/health/ retorna ok", async ({ request }) => {
    const res = await request.get("/api/whatsapp/health/");
    expect(res.ok()).toBeTruthy();
    const data = await res.json();
    expect(data.status).toBe("ok");
    expect(data.service).toBe("jury_ai_whatsapp");
  });
});
