# Copie le bon setup.cfg et exécute behave

run:
	@echo "Usage: make dev | make test"

default:
	@cp setup.default.cfg setup.cfg


dev:
	@cp setup.dev.cfg setup.cfg
	@echo "=== Profil DEV ==="
	behave

test:
	@cp setup.test.cfg setup.cfg
	@echo "=== Profil Test ==="
	behave
