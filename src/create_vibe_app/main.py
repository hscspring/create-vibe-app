import typer
import shutil
import os
from pathlib import Path
from rich import print
from rich.console import Console
from rich.prompt import Prompt
import subprocess
import pkg_resources

app = typer.Typer(help="Create a new Vibe Coding project")
console = Console()

def init_git(project_path: Path):
    """Initialize a git repository in the project path."""
    try:
        subprocess.run(["git", "init"], cwd=project_path, check=True, capture_output=True)
        print(f"[green]Initialized git repository in {project_path}[/green]")
    except subprocess.CalledProcessError:
        print("[yellow]Failed to initialize git repository. Please run 'git init' manually.[/yellow]")
    except FileNotFoundError:
        print("[yellow]Git not found. Skipping git initialization.[/yellow]")

@app.command()
def main(project_name: str = typer.Argument(None, help="The name of the project to create")):
    """
    Scaffold a new Vibe Coding project.
    """
    if not project_name:
        project_name = Prompt.ask("Project name", default="my-vibe-project")

    project_path = Path(os.getcwd()) / project_name

    if project_path.exists():
        print(f"[red]Error: Directory '{project_name}' already exists.[/red]")
        raise typer.Exit(code=1)

    # Locate the template directory within the package
    # We assume 'templates/vibe-default' is relative to this file's directory
    # But since we installed it as package data, we need to be careful.
    # Using __file__ logic:
    current_dir = Path(__file__).parent
    template_source = current_dir / "templates" / "vibe-default"

    if not template_source.exists():
        # Fallback for development mode if running from src directly
        # But if installed via pip, MANIFEST.in should ensure it's there.
        print(f"[red]Critical Error: Template not found at {template_source}[/red]")
        raise typer.Exit(code=1)

    print(f"[bold blue]Creating Vibe project '{project_name}'...[/bold blue]")
    
    try:
        shutil.copytree(template_source, project_path)
    except Exception as e:
        print(f"[red]Error copying template: {e}[/red]")
        raise typer.Exit(code=1)

    init_git(project_path)

    print("\n[bold green]✅ Success! Created project at:[/bold green] " + str(project_path))
    print("\n[bold]📖 Next steps:[/bold]")
    print(f"   cd {project_name}")
    print("   code .  # or your preferred IDE")
    print("\n[bold]💡 In your AI assistant, try:[/bold]")
    print('   "Read MAIN.md, then help me build [your idea]"')

if __name__ == "__main__":
    app()

