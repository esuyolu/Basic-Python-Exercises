class CommandPrompt:
    def __init__(self, prompt):
        self._prompt = prompt

    def run(self):
        while True:
            self._prompt = input().strip()

            if self._prompt == 'quit':
                break

            print(self._prompt[::-1])


cp = CommandPrompt('CSD')
cp.run()
