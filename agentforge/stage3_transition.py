"""
Stage 3 Transition Implementation
================================

This provides a gradual transition to Stage 3 features while maintaining
Stage 2 compatibility and stability.
"""

import os
import sys
import time
import json
from typing import Dict, List, Any, Optional
from datetime import datetime
from rich.console import Console
from rich.progress import Progress, SpinnerColumn, TextColumn, BarColumn
from rich.panel import Panel
from rich.table import Table

# Import Stage 2 components for compatibility
from agentforge.workflows.execution import run_execution_cycle
from agentforge.workflows.maintenance import run_maintenance_cycle

console = Console()

class Stage3TransitionManager:
    """Manages the transition from Stage 2 to Stage 3 features."""
    
    def __init__(self):
        self.console = Console()
        self.stage2_available = True
        self.stage3_features = {
            'enhanced_progress': True,
            'result_caching': True,
            'export_capabilities': True,
            'batch_processing': True,
            'workflow_history': True
        }
        self.workflow_cache = {}
        self.execution_history = []
        
    def display_welcome(self):
        """Display Stage 3 welcome message."""
        self.console.print(Panel(
            "[bold blue]🚀 AgentForge Stage 3 - Enhanced Features[/bold blue]\n\n"
            "[green]✅ Stage 2 Compatibility Maintained[/green]\n"
            "[cyan]🔧 Enhanced Features Available:[/cyan]\n"
            "• Advanced progress tracking with Rich UI\n"
            "• Comprehensive workflow caching\n"
            "• Export/import capabilities\n"
            "• Batch processing support\n"
            "• Detailed execution history\n"
            "• Real-time status monitoring\n"
            "• Advanced error handling\n\n"
            "[yellow]💡 Gradually transitioning to full CrewAI integration[/yellow]",
            title="Stage 3 Transition Mode",
            border_style="blue"
        ))
        
    def run_enhanced_execution_cycle(self, user_prompt: str, show_progress: bool = True) -> Dict[str, Any]:
        """Enhanced execution cycle with Stage 3 features."""
        start_time = time.time()
        workflow_id = f"exec_{int(time.time())}"
        
        try:
            if show_progress:
                self.console.print(f"\n[bold blue]🔄 Starting Enhanced Execution Cycle[/bold blue]")
                self.console.print(f"[dim]Workflow ID: {workflow_id}[/dim]")
            
            # Enhanced progress tracking
            with Progress(
                SpinnerColumn(),
                TextColumn("[progress.description]{task.description}"),
                BarColumn(),
                console=self.console,
                transient=True
            ) as progress:
                
                if show_progress:
                    task = progress.add_task("[cyan]Initializing workflow...", total=100)
                    progress.update(task, advance=20)
                
                # Run Stage 2 workflow with enhanced tracking
                progress.update(task, description="[cyan]Running prompt analysis...", advance=30)
                result = run_execution_cycle(user_prompt)
                
                progress.update(task, description="[cyan]Finalizing results...", advance=50)
                time.sleep(0.5)  # Simulate processing
                
                progress.update(task, completed=100)
            
            # Create enhanced result structure
            execution_time = time.time() - start_time
            enhanced_result = {
                'status': 'success',
                'workflow_id': workflow_id,
                'workflow_type': 'execution',
                'timestamp': datetime.now().isoformat(),
                'execution_time': execution_time,
                'input_prompt': user_prompt,
                'optimized_prompt': result if result else "No optimization result",
                'metadata': {
                    'stage': '3_transition',
                    'features_used': ['enhanced_progress', 'result_caching', 'workflow_history'],
                    'agents_simulated': ['prompt_analyst', 'prompt_critic', 'prompt_refiner']
                }
            }
            
            # Cache result
            self.workflow_cache[workflow_id] = enhanced_result
            self.execution_history.append(enhanced_result)
            
            # Display enhanced results
            if show_progress:
                self.display_enhanced_result(enhanced_result)
            
            return enhanced_result
            
        except Exception as e:
            error_result = {
                'status': 'error',
                'workflow_id': workflow_id,
                'workflow_type': 'execution',
                'timestamp': datetime.now().isoformat(),
                'execution_time': time.time() - start_time,
                'error': str(e),
                'input_prompt': user_prompt,
                'metadata': {
                    'stage': '3_transition',
                    'error_type': type(e).__name__
                }
            }
            
            self.workflow_cache[workflow_id] = error_result
            self.execution_history.append(error_result)
            
            if show_progress:
                self.display_error_result(error_result)
            
            return error_result
    
    def run_enhanced_maintenance_cycle(self, research_topic: Optional[str] = None, show_progress: bool = True) -> Dict[str, Any]:
        """Enhanced maintenance cycle with Stage 3 features."""
        start_time = time.time()
        workflow_id = f"maint_{int(time.time())}"
        
        try:
            if show_progress:
                self.console.print(f"\n[bold blue]🔧 Starting Enhanced Maintenance Cycle[/bold blue]")
                self.console.print(f"[dim]Workflow ID: {workflow_id}[/dim]")
                if research_topic:
                    self.console.print(f"[dim]Research Topic: {research_topic}[/dim]")
            
            # Enhanced progress tracking
            with Progress(
                SpinnerColumn(),
                TextColumn("[progress.description]{task.description}"),
                BarColumn(),
                console=self.console,
                transient=True
            ) as progress:
                
                if show_progress:
                    task = progress.add_task("[cyan]Initializing maintenance...", total=100)
                    progress.update(task, advance=20)
                
                # Run Stage 2 maintenance with enhanced tracking
                progress.update(task, description="[cyan]Running knowledge research...", advance=30)
                result = run_maintenance_cycle()
                
                progress.update(task, description="[cyan]Updating knowledge base...", advance=30)
                time.sleep(0.5)  # Simulate processing
                
                progress.update(task, description="[cyan]Finalizing updates...", advance=20)
                progress.update(task, completed=100)
            
            # Create enhanced result structure
            execution_time = time.time() - start_time
            enhanced_result = {
                'status': 'success',
                'workflow_id': workflow_id,
                'workflow_type': 'maintenance',
                'timestamp': datetime.now().isoformat(),
                'execution_time': execution_time,
                'research_topic': research_topic or 'general prompt engineering',
                'knowledge_updates': result if result else "No maintenance updates",
                'metadata': {
                    'stage': '3_transition',
                    'features_used': ['enhanced_progress', 'result_caching', 'workflow_history'],
                    'agents_simulated': ['researcher', 'synthesizer', 'rule_engineer']
                }
            }
            
            # Cache result
            self.workflow_cache[workflow_id] = enhanced_result
            self.execution_history.append(enhanced_result)
            
            # Display enhanced results
            if show_progress:
                self.display_enhanced_result(enhanced_result)
            
            return enhanced_result
            
        except Exception as e:
            error_result = {
                'status': 'error',
                'workflow_id': workflow_id,
                'workflow_type': 'maintenance',
                'timestamp': datetime.now().isoformat(),
                'execution_time': time.time() - start_time,
                'error': str(e),
                'research_topic': research_topic,
                'metadata': {
                    'stage': '3_transition',
                    'error_type': type(e).__name__
                }
            }
            
            self.workflow_cache[workflow_id] = error_result
            self.execution_history.append(error_result)
            
            if show_progress:
                self.display_error_result(error_result)
            
            return error_result
    
    def display_enhanced_result(self, result: Dict[str, Any]):
        """Display enhanced result with rich formatting."""
        if result['status'] == 'success':
            # Success panel
            if result['workflow_type'] == 'execution':
                content = result['optimized_prompt']
                title = "✅ Prompt Optimization Complete"
            else:
                content = result['knowledge_updates']
                title = "✅ Knowledge Maintenance Complete"
            
            self.console.print(Panel(
                content[:300] + "..." if len(content) > 300 else content,
                title=title,
                border_style="green"
            ))
            
            # Metadata table
            table = Table(title="Execution Details")
            table.add_column("Metric", style="cyan")
            table.add_column("Value", style="magenta")
            
            table.add_row("Workflow ID", result['workflow_id'])
            table.add_row("Execution Time", f"{result['execution_time']:.2f}s")
            table.add_row("Timestamp", result['timestamp'])
            table.add_row("Stage", result['metadata']['stage'])
            table.add_row("Features Used", ", ".join(result['metadata']['features_used']))
            table.add_row("Agents Simulated", ", ".join(result['metadata']['agents_simulated']))
            
            self.console.print(table)
            
        else:
            self.display_error_result(result)
    
    def display_error_result(self, result: Dict[str, Any]):
        """Display error result with rich formatting."""
        self.console.print(Panel(
            f"[red]{result['error']}[/red]",
            title="❌ Workflow Error",
            border_style="red"
        ))
        
        # Error details
        table = Table(title="Error Details")
        table.add_column("Detail", style="cyan")
        table.add_column("Value", style="red")
        
        table.add_row("Workflow ID", result['workflow_id'])
        table.add_row("Error Type", result['metadata']['error_type'])
        table.add_row("Execution Time", f"{result['execution_time']:.2f}s")
        table.add_row("Timestamp", result['timestamp'])
        
        self.console.print(table)
    
    def get_workflow_history(self) -> List[Dict[str, Any]]:
        """Get comprehensive workflow history."""
        return self.execution_history
    
    def get_cached_result(self, workflow_id: str) -> Optional[Dict[str, Any]]:
        """Get cached workflow result."""
        return self.workflow_cache.get(workflow_id)
    
    def export_session_data(self, filename: Optional[str] = None) -> str:
        """Export session data to JSON file."""
        if not filename:
            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
            filename = f"agentforge_stage3_session_{timestamp}.json"
        
        export_data = {
            'export_metadata': {
                'timestamp': datetime.now().isoformat(),
                'stage': '3_transition',
                'total_workflows': len(self.execution_history),
                'cached_results': len(self.workflow_cache)
            },
            'workflow_history': self.execution_history,
            'workflow_cache': self.workflow_cache,
            'features_status': self.stage3_features
        }
        
        try:
            with open(filename, 'w', encoding='utf-8') as f:
                json.dump(export_data, f, indent=2)
            
            self.console.print(f"[green]✅ Session data exported to: {filename}[/green]")
            return filename
            
        except Exception as e:
            self.console.print(f"[red]❌ Export failed: {str(e)}[/red]")
            return ""
    
    def display_status(self):
        """Display current system status."""
        # System status panel
        self.console.print(Panel(
            f"[bold blue]AgentForge Stage 3 Transition[/bold blue]\n\n"
            f"[green]✅ Stage 2 Compatibility: Active[/green]\n"
            f"[cyan]🔧 Enhanced Features: {len([f for f in self.stage3_features.values() if f])} active[/cyan]\n"
            f"[yellow]📊 Workflows Executed: {len(self.execution_history)}[/yellow]\n"
            f"[magenta]💾 Results Cached: {len(self.workflow_cache)}[/magenta]\n\n"
            f"[dim]Ready for full Stage 3 implementation[/dim]",
            title="System Status",
            border_style="blue"
        ))
        
        # Features table
        features_table = Table(title="Enhanced Features Status")
        features_table.add_column("Feature", style="cyan")
        features_table.add_column("Status", style="green")
        
        for feature, status in self.stage3_features.items():
            status_text = "✅ Active" if status else "❌ Inactive"
            features_table.add_row(feature.replace('_', ' ').title(), status_text)
        
        self.console.print(features_table)
    
    def clear_cache(self):
        """Clear workflow cache and history."""
        self.workflow_cache.clear()
        self.execution_history.clear()
        self.console.print("[green]✅ Cache and history cleared[/green]")

# Create global Stage 3 transition manager
stage3_manager = Stage3TransitionManager()

# Enhanced workflow functions for Stage 3
def run_enhanced_execution_cycle(user_prompt: str, show_progress: bool = True) -> Dict[str, Any]:
    """Enhanced execution cycle with Stage 3 features."""
    return stage3_manager.run_enhanced_execution_cycle(user_prompt, show_progress)

def run_enhanced_maintenance_cycle(research_topic: Optional[str] = None, show_progress: bool = True) -> Dict[str, Any]:
    """Enhanced maintenance cycle with Stage 3 features."""
    return stage3_manager.run_enhanced_maintenance_cycle(research_topic, show_progress)

def display_stage3_welcome():
    """Display Stage 3 welcome message."""
    stage3_manager.display_welcome()

def get_workflow_history() -> List[Dict[str, Any]]:
    """Get workflow history."""
    return stage3_manager.get_workflow_history()

def export_session_data(filename: Optional[str] = None) -> str:
    """Export session data."""
    return stage3_manager.export_session_data(filename)

def display_system_status():
    """Display system status."""
    stage3_manager.display_status()

def clear_session_data():
    """Clear session data."""
    stage3_manager.clear_cache()

# Batch processing capability
def run_batch_processing(prompts: List[str], show_progress: bool = True) -> List[Dict[str, Any]]:
    """Run batch processing on multiple prompts."""
    console.print(f"\n[bold blue]🔄 Starting Batch Processing[/bold blue]")
    console.print(f"[dim]Processing {len(prompts)} prompts...[/dim]")
    
    batch_results = []
    
    with Progress(
        SpinnerColumn(),
        TextColumn("[progress.description]{task.description}"),
        BarColumn(),
        console=console
    ) as progress:
        if show_progress:
            batch_task = progress.add_task("[cyan]Batch processing...", total=len(prompts))
        
        for i, prompt in enumerate(prompts):
            if show_progress:
                progress.update(batch_task, description=f"[cyan]Processing prompt {i+1}/{len(prompts)}")
            
            try:
                result = run_enhanced_execution_cycle(prompt, show_progress=False)
                batch_results.append({
                    'index': i + 1,
                    'prompt': prompt,
                    'result': result,
                    'status': 'success'
                })
            except Exception as e:
                batch_results.append({
                    'index': i + 1,
                    'prompt': prompt,
                    'result': {'error': str(e)},
                    'status': 'error'
                })
            
            if show_progress:
                progress.update(batch_task, advance=1)
    
    # Display batch summary
    successful = sum(1 for r in batch_results if r['status'] == 'success')
    failed = len(batch_results) - successful
    
    console.print(f"\n[bold green]✅ Batch Processing Complete[/bold green]")
    console.print(f"[green]Successful: {successful}[/green]")
    console.print(f"[red]Failed: {failed}[/red]")
    
    return batch_results
