"""
AgentForge Stage 3 Enhanced Main Entry Point
===========================================

Enhanced main entry point that provides Stage 3 features while maintaining
Stage 2 compatibility and stability.
"""

import argparse
import sys
from typing import List, Optional
from rich.console import Console
from rich.prompt import Prompt, Confirm
from rich.panel import Panel

# Import Stage 3 transition components
from agentforge.stage3_transition import (
    display_stage3_welcome,
    run_enhanced_execution_cycle,
    run_enhanced_maintenance_cycle,
    run_batch_processing,
    display_system_status,
    get_workflow_history,
    export_session_data,
    clear_session_data
)

console = Console()

def create_enhanced_cli():
    """Create enhanced command-line interface."""
    parser = argparse.ArgumentParser(
        description="AgentForge Stage 3 - Enhanced AI Prompt Optimization",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  python enhanced_main.py --optimize "Create a Python function"
  python enhanced_main.py --research "latest AI techniques"
  python enhanced_main.py --batch prompts.txt
  python enhanced_main.py --interactive
  python enhanced_main.py --status
        """
    )
    
    # Main operations
    parser.add_argument('--optimize', '-o', type=str, 
                       help='Optimize a prompt directly')
    parser.add_argument('--research', '-r', type=str, nargs='?', const='',
                       help='Run research workflow (optional topic)')
    parser.add_argument('--batch', '-b', type=str,
                       help='Process batch file (one prompt per line)')
    parser.add_argument('--interactive', '-i', action='store_true',
                       help='Start interactive mode')
    
    # System operations
    parser.add_argument('--status', '-s', action='store_true',
                       help='Show system status')
    parser.add_argument('--history', action='store_true',
                       help='Show workflow history')
    parser.add_argument('--export', type=str, nargs='?', const='',
                       help='Export session data (optional filename)')
    parser.add_argument('--clear', action='store_true',
                       help='Clear session data')
    
    # Options
    parser.add_argument('--no-progress', action='store_true',
                       help='Disable progress display')
    parser.add_argument('--output', '-f', type=str,
                       help='Output file for results')
    parser.add_argument('--verbose', '-v', action='store_true',
                       help='Verbose output')
    
    return parser

def handle_optimize_command(prompt: str, args):
    """Handle optimize command."""
    console.print(f"\n[bold blue]🔄 Optimizing Prompt[/bold blue]")
    console.print(Panel(prompt, title="Input Prompt", border_style="blue"))
    
    try:
        result = run_enhanced_execution_cycle(prompt, show_progress=not args.no_progress)
        
        if args.output:
            with open(args.output, 'w', encoding='utf-8') as f:
                if result['status'] == 'success':
                    f.write(result['optimized_prompt'])
                else:
                    f.write(f"Error: {result['error']}")
            console.print(f"[green]✅ Result saved to: {args.output}[/green]")
        
        return result
        
    except Exception as e:
        console.print(f"[red]❌ Optimization failed: {str(e)}[/red]")
        return None

def handle_research_command(topic: Optional[str], args):
    """Handle research command."""
    console.print(f"\n[bold blue]🔍 Running Research Workflow[/bold blue]")
    if topic:
        console.print(f"[dim]Topic: {topic}[/dim]")
    
    try:
        result = run_enhanced_maintenance_cycle(topic, show_progress=not args.no_progress)
        
        if args.output:
            with open(args.output, 'w', encoding='utf-8') as f:
                if result['status'] == 'success':
                    f.write(result['knowledge_updates'])
                else:
                    f.write(f"Error: {result['error']}")
            console.print(f"[green]✅ Result saved to: {args.output}[/green]")
        
        return result
        
    except Exception as e:
        console.print(f"[red]❌ Research failed: {str(e)}[/red]")
        return None

def handle_batch_command(filepath: str, args):
    """Handle batch processing command."""
    try:
        # Read prompts from file
        with open(filepath, 'r', encoding='utf-8') as f:
            prompts = [line.strip() for line in f.readlines() if line.strip()]
        
        if not prompts:
            console.print(f"[red]❌ No prompts found in file: {filepath}[/red]")
            return
        
        console.print(f"\n[bold blue]📦 Batch Processing[/bold blue]")
        console.print(f"[dim]File: {filepath}[/dim]")
        console.print(f"[dim]Prompts: {len(prompts)}[/dim]")
        
        # Run batch processing
        batch_results = run_batch_processing(prompts, show_progress=not args.no_progress)
        
        # Export batch results
        if args.output:
            output_file = args.output
        else:
            from datetime import datetime
            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
            output_file = f"batch_results_{timestamp}.json"
        
        import json
        with open(output_file, 'w', encoding='utf-8') as f:
            json.dump({
                'source_file': filepath,
                'timestamp': datetime.now().isoformat(),
                'results': batch_results,
                'summary': {
                    'total': len(batch_results),
                    'successful': sum(1 for r in batch_results if r['status'] == 'success'),
                    'failed': sum(1 for r in batch_results if r['status'] == 'error')
                }
            }, f, indent=2)
        
        console.print(f"[green]✅ Batch results saved to: {output_file}[/green]")
        
    except FileNotFoundError:
        console.print(f"[red]❌ File not found: {filepath}[/red]")
    except Exception as e:
        console.print(f"[red]❌ Batch processing failed: {str(e)}[/red]")

def handle_interactive_mode():
    """Handle interactive mode."""
    console.print(f"\n[bold blue]🎮 Interactive Mode[/bold blue]")
    console.print("[dim]Type 'help' for commands, 'exit' to quit[/dim]")
    
    while True:
        try:
            command = Prompt.ask("\n[bold cyan]AgentForge>[/bold cyan]", default="help")
            
            if command.lower() in ['exit', 'quit']:
                console.print("[bold blue]Goodbye! 👋[/bold blue]")
                break
            
            elif command.lower() == 'help':
                console.print(Panel(
                    "[bold]Available Commands:[/bold]\n\n"
                    "[cyan]optimize[/cyan] - Optimize a prompt\n"
                    "[cyan]research[/cyan] - Run research workflow\n"
                    "[cyan]status[/cyan] - Show system status\n"
                    "[cyan]history[/cyan] - Show workflow history\n"
                    "[cyan]export[/cyan] - Export session data\n"
                    "[cyan]clear[/cyan] - Clear session data\n"
                    "[cyan]exit[/cyan] - Exit interactive mode",
                    title="Interactive Help",
                    border_style="green"
                ))
            
            elif command.lower() == 'optimize':
                prompt = Prompt.ask("Enter prompt to optimize")
                if prompt:
                    run_enhanced_execution_cycle(prompt)
            
            elif command.lower() == 'research':
                topic = Prompt.ask("Enter research topic (or press Enter for general)", default="")
                run_enhanced_maintenance_cycle(topic if topic else None)
            
            elif command.lower() == 'status':
                display_system_status()
            
            elif command.lower() == 'history':
                history = get_workflow_history()
                if history:
                    console.print(f"[green]📋 {len(history)} workflows in history[/green]")
                    for i, item in enumerate(history[-5:], 1):  # Show last 5
                        status = "✅" if item['status'] == 'success' else "❌"
                        console.print(f"{status} [{item['timestamp'][:19]}] {item['workflow_type']} - {item['workflow_id']}")
                else:
                    console.print("[yellow]No workflow history available[/yellow]")
            
            elif command.lower() == 'export':
                filename = Prompt.ask("Enter filename (or press Enter for auto)", default="")
                export_session_data(filename if filename else None)
            
            elif command.lower() == 'clear':
                if Confirm.ask("Clear all session data?"):
                    clear_session_data()
            
            else:
                console.print(f"[red]Unknown command: {command}[/red]")
                console.print("[dim]Type 'help' for available commands[/dim]")
                
        except KeyboardInterrupt:
            console.print("\n[bold blue]Goodbye! 👋[/bold blue]")
            break
        except Exception as e:
            console.print(f"[red]❌ Error: {str(e)}[/red]")

def main():
    """Main entry point for enhanced AgentForge."""
    # Display welcome
    display_stage3_welcome()
    
    # Parse arguments
    parser = create_enhanced_cli()
    args = parser.parse_args()
    
    # Handle commands
    if args.optimize:
        handle_optimize_command(args.optimize, args)
    
    elif args.research is not None:
        topic = args.research if args.research else None
        handle_research_command(topic, args)
    
    elif args.batch:
        handle_batch_command(args.batch, args)
    
    elif args.status:
        display_system_status()
    
    elif args.history:
        history = get_workflow_history()
        if history:
            console.print(f"[green]📋 Workflow History ({len(history)} items)[/green]")
            for item in history:
                status = "✅" if item['status'] == 'success' else "❌"
                console.print(f"{status} [{item['timestamp'][:19]}] {item['workflow_type']} - {item['workflow_id']}")
        else:
            console.print("[yellow]No workflow history available[/yellow]")
    
    elif args.export is not None:
        filename = args.export if args.export else None
        export_session_data(filename)
    
    elif args.clear:
        if Confirm.ask("Clear all session data?"):
            clear_session_data()
    
    elif args.interactive:
        handle_interactive_mode()
    
    else:
        # Default to interactive mode
        handle_interactive_mode()

if __name__ == "__main__":
    main()
