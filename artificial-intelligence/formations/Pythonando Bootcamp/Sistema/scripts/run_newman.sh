#!/usr/bin/env bash
# Executa a collection Postman do Jury AI com Newman.
# Uso: ./scripts/run_newman.sh [collection.json] [environment.json]
# Requer: servidor Django rodando em base_url (ex.: http://localhost:8000)

COLLECTION=${1:-postman/collection.json}
ENV=${2:-postman/environment.json}
REPORT_DIR=${REPORT_DIR:-reports/postman}
ROOT=$(cd "$(dirname "$0")/.." && pwd)

cd "$ROOT"
mkdir -p "$REPORT_DIR"

if ! command -v npx &>/dev/null; then
  echo "npx não encontrado. Instale Node.js e tente novamente."
  exit 1
fi

npx newman run "$COLLECTION" -e "$ENV" \
  --reporters cli,junit,html \
  --reporter-junit-export "$REPORT_DIR/junit-results.xml" \
  --reporter-html-export "$REPORT_DIR/report.html" \
  --ignore-redirects

EXIT_CODE=$?
if [ $EXIT_CODE -ne 0 ]; then
  echo "Newman falhou (exit $EXIT_CODE)"
  exit $EXIT_CODE
fi
echo "Newman concluído. Relatórios em $REPORT_DIR/"
