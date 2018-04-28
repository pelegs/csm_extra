NAME = "extra"
TEX = pdflatex -shell-escape
RM = rm -rf
PYLIB = "pythontex-files-$(NAME)"
PYTEX = pythontex3
PYTEX_FILE = "$(NAME).pytxcode"

extra:
	$(RM) $(PYLIB) && $(TEX) $(NAME) && $(PYTEX) $(PYTEX_FILE) && $(TEX) $(NAME)

read:
	evince "$(NAME).pdf"
