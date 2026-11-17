// Ralph TUI agent plugin that runs the Command Code CLI (`cmd -p`) headless for the research turns.
// Install: copy this file to ~/.config/ralph-tui/plugins/agents/ and set `agent = "command-code-research"`
// in .ralph-tui/config.toml. The import below must be the absolute path of your global
// ralph-tui install (an ES import does not expand `~`); it was replaced here for privacy.
// detect() is hard-coded: it reports the CLI as available without probing it.
import { BaseAgentPlugin } from "<HOME>/.bun/install/global/node_modules/ralph-tui/dist/index.js";

class CommandCodeResearchPlugin extends BaseAgentPlugin {
  meta = {
    id: "command-code-research",
    name: "Command Code (research, all tools)",
    description: "Command Code CLI (cmd -p), works on the Go plan",
    version: "1.0.0",
    author: "local",
    defaultCommand: "cmd",
    supportsStreaming: false,
    supportsInterrupt: true,
    supportsFileContext: false,
    supportsSubagentTracing: false,
  };
  model;
  async initialize(config) {
    await super.initialize(config);
    if (typeof config.model === "string" && config.model) this.model = config.model;
  }
  async detect() {
    return { available: true, version: "1.9.0", executablePath: this.commandPath ?? "cmd" };
  }
  buildArgs() {
    const args = ["-p", "--no-session", "--yolo", "--skip-onboarding", "--no-auto-update", "--tools-all", "--max-turns", "250"];
    if (this.model) args.push("-m", this.model);
    return args;
  }
  getStdinInput(prompt) {
    return prompt;
  }
}

export default () => new CommandCodeResearchPlugin();
