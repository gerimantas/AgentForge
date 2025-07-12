"""
AgentForge Stage 3 Enhanced Main Entry Point
===========================================

Main entry point for Stage 3 enhanced AgentForge with full feature integration.
"""

import sys
import argparse
from rich.console import Console
from rich.prompt import Prompt, Confirm
from rich.panel import Panel

# Import Stage 3 enhanced components
from agentforge.stage3_enhanced import (
    run_stage3_execution_cycle,
    get_stage3_workflow_history,
    clear_stage3_cache,
    display_stage3_status,
    enhanced_workflow_manager
)

console = Console()

def main():
    """Main entry point for Stage 3 enhanced AgentForge."""
    
    # Display Stage 3 welcome
    console.print(Panel(
        "[bold blue]🚀 AgentForge Stage 3 Enhanced[/bold blue]\n\n"
        "[green]✅ Full Stage 3 Implementation Active[/green]\n"
        "[cyan]🎯 Advanced Multi-Agent Workflows Ready[/cyan]\n"
        "[yellow]📊 Performance Tracking Enabled[/yellow]\n"
        "[magenta]🔧 Enhanced Features Operational[/magenta]\n\n"
        "[bold]Enhanced Capabilities:[/bold]\n"
        "• Advanced progress tracking with real-time updates\n"
        "• Multi-agent synthesis and coordination\n"
        "• Performance metrics and execution tracking\n"
        "• Enhanced error handling and recovery\n"
        "• Comprehensive workflow history and caching\n"
        "• Advanced result formatting and visualization\n\n"
        "[dim]Ready for production deployment[/dim]",
        title="Stage 3 Enhanced System",
        border_style="blue"
    ))
    
    # Create argument parser
    parser = argparse.ArgumentParser(
        description="AgentForge Stage 3 Enhanced - Advanced AI Prompt Optimization",
        formatter_class=argparse.RawDescriptionHelpFormatter
    )
    
    # Add arguments
    parser.add_argument('--optimize', '-o', type=str, 
                       help='Optimize a prompt with Stage 3 enhanced features')
    parser.add_argument('--interactive', '-i', action='store_true',
                       help='Start interactive Stage 3 enhanced mode')
    parser.add_argument('--status', '-s', action='store_true',
                       help='Show Stage 3 enhanced system status')
    parser.add_argument('--history', action='store_true',
                       help='Show Stage 3 enhanced workflow history')
    parser.add_argument('--clear', action='store_true',
                       help='Clear Stage 3 enhanced cache')
    parser.add_argument('--test', action='store_true',
                       help='Run Stage 3 enhanced test suite')
    parser.add_argument('--no-progress', action='store_true',
                       help='Disable progress display')
    
    # Parse arguments
    args = parser.parse_args()
    
    # Handle commands
    if args.optimize:
        console.print(f"\n[bold blue]🎯 Stage 3 Enhanced Optimization[/bold blue]")
        console.print(Panel(args.optimize, title="Input Prompt", border_style="blue"))
        
        result = run_stage3_execution_cycle(args.optimize, show_progress=not args.no_progress)
        
        if result['status'] == 'success':
            console.print(f"\n[bold green]✅ Stage 3 Enhanced Optimization Complete[/bold green]")
        else:
            console.print(f"\n[bold red]❌ Stage 3 Enhanced Optimization Failed[/bold red]")
    
    elif args.status:
        display_stage3_status()
    
    elif args.history:
        history = get_stage3_workflow_history()
        if history:
            console.print(f"\n[bold blue]📋 Stage 3 Enhanced Workflow History[/bold blue]")
            console.print(f"[dim]Total workflows: {len(history)}[/dim]")
            
            for i, item in enumerate(history[-10:], 1):  # Show last 10
                status = "✅" if item['status'] == 'success' else "❌"
                console.print(f"{status} [{item['timestamp'][:19]}] {item['workflow_type']} - {item['workflow_id']}")
        else:
            console.print("[yellow]No Stage 3 enhanced workflow history available[/yellow]")
    
    elif args.clear:
        if Confirm.ask("Clear all Stage 3 enhanced cache and history?"):
            clear_stage3_cache()
            console.print("[green]✅ Stage 3 enhanced cache cleared[/green]")
    
    elif args.test:
        console.print("[bold blue]🧪 Running Stage 3 Enhanced Test Suite[/bold blue]")
        
        # Test basic functionality
        test_prompt = "Create a comprehensive tutorial for learning Python programming"
        result = run_stage3_execution_cycle(test_prompt, show_progress=True)
        
        console.print(f"\n[bold green]✅ Stage 3 Enhanced Test Complete[/bold green]")
        console.print(f"[dim]Status: {result['status']}[/dim]")
        console.print(f"[dim]Execution Time: {result['execution_time']:.2f}s[/dim]")
        console.print(f"[dim]Agent Executions: {result['metadata']['total_agent_executions']}[/dim]")
        
    elif args.interactive:
        run_interactive_mode()
    
    else:
        # Default to interactive mode
        run_interactive_mode()

def run_interactive_mode():
    """Run Stage 3 enhanced interactive mode."""
    console.print(f"\n[bold blue]🎮 Stage 3 Enhanced Interactive Mode[/bold blue]")
    console.print("[dim]Type 'help' for commands, 'exit' to quit[/dim]")
    
    while True:
        try:
            command = Prompt.ask("\n[bold cyan]AgentForge Stage 3>[/bold cyan]", default="help")
            
            if command.lower() in ['exit', 'quit']:
                console.print("[bold blue]Goodbye from Stage 3! 👋[/bold blue]")
                break
            
            elif command.lower() == 'help':
                console.print(Panel(
                    "[bold]Stage 3 Enhanced Commands:[/bold]\n\n"
                    "[cyan]optimize[/cyan] - Run Stage 3 enhanced prompt optimization\n"
                    "[cyan]status[/cyan] - Show Stage 3 enhanced system status\n"
                    "[cyan]history[/cyan] - Show Stage 3 enhanced workflow history\n"
                    "[cyan]clear[/cyan] - Clear Stage 3 enhanced cache\n"
                    "[cyan]test[/cyan] - Run Stage 3 enhanced test\n"
                    "[cyan]demo[/cyan] - Run Stage 3 enhanced demonstration\n"
                    "[cyan]exit[/cyan] - Exit Stage 3 enhanced interactive mode\n\n"
                    "[bold]Enhanced Features:[/bold]\n"
                    "• Advanced multi-agent coordination\n"
                    "• Real-time progress tracking\n"
                    "• Performance metrics collection\n"
                    "• Comprehensive error handling\n"
                    "• Workflow history and caching",
                    title="Stage 3 Enhanced Interactive Help",
                    border_style="green"
                ))
            
            elif command.lower() == 'optimize':
                prompt = Prompt.ask("Enter prompt to optimize with Stage 3 enhanced features")
                if prompt:
                    result = run_stage3_execution_cycle(prompt, show_progress=True)
                    if result['status'] == 'success':
                        console.print(f"[green]✅ Stage 3 enhanced optimization completed in {result['execution_time']:.2f}s[/green]")
                    else:
                        console.print(f"[red]❌ Stage 3 enhanced optimization failed[/red]")
            
            elif command.lower() == 'status':
                display_stage3_status()
            
            elif command.lower() == 'history':
                history = get_stage3_workflow_history()
                if history:
                    console.print(f"[green]📋 Stage 3 Enhanced History ({len(history)} workflows)[/green]")
                    for item in history[-5:]:  # Show last 5
                        status = "✅" if item['status'] == 'success' else "❌"
                        console.print(f"{status} [{item['timestamp'][:19]}] {item['workflow_type']} - {item['workflow_id']}")
                else:
                    console.print("[yellow]No Stage 3 enhanced workflow history available[/yellow]")
            
            elif command.lower() == 'clear':
                if Confirm.ask("Clear Stage 3 enhanced cache?"):
                    clear_stage3_cache()
                    console.print("[green]✅ Stage 3 enhanced cache cleared[/green]")
            
            elif command.lower() == 'test':
                console.print("[bold blue]🧪 Running Stage 3 Enhanced Test[/bold blue]")
                test_prompt = "Explain machine learning concepts for beginners"
                result = run_stage3_execution_cycle(test_prompt, show_progress=True)
                console.print(f"[green]✅ Test completed - Status: {result['status']}[/green]")
            
            elif command.lower() == 'demo':
                console.print("[bold blue]🎬 Stage 3 Enhanced Demonstration[/bold blue]")
                
                demo_prompts = [
                    "Create a Python tutorial for beginners",
                    "Explain artificial intelligence concepts",
                    "Design a web development roadmap"
                ]
                
                console.print(f"[dim]Running {len(demo_prompts)} demonstration workflows...[/dim]")
                
                for i, prompt in enumerate(demo_prompts, 1):
                    console.print(f"\n[cyan]Demo {i}/{len(demo_prompts)}: {prompt}[/cyan]")
                    result = run_stage3_execution_cycle(prompt, show_progress=True)
                    console.print(f"[green]✅ Demo {i} completed in {result['execution_time']:.2f}s[/green]")
                
                console.print(f"\n[bold green]✅ Stage 3 Enhanced Demonstration Complete[/bold green]")
                
                # Show summary
                history = get_stage3_workflow_history()
                recent_workflows = history[-len(demo_prompts):]
                avg_time = sum(w['execution_time'] for w in recent_workflows) / len(recent_workflows)
                total_executions = sum(w['metadata']['total_agent_executions'] for w in recent_workflows)
                
                console.print(f"[dim]Average execution time: {avg_time:.2f}s[/dim]")
                console.print(f"[dim]Total agent executions: {total_executions}[/dim]")
            
            else:
                console.print(f"[red]Unknown command: {command}[/red]")
                console.print("[dim]Type 'help' for available commands[/dim]")
                
        except KeyboardInterrupt:
            console.print("\n[bold blue]Goodbye from Stage 3! 👋[/bold blue]")
            break
        except Exception as e:
            console.print(f"[red]❌ Error: {str(e)}[/red]")

if __name__ == "__main__":
    main()
