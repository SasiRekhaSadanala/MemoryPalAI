# frontend/components/graph_view.py
import streamlit as st
from streamlit_agraph import agraph, Node, Edge, Config

def render_knowledge_graph(graph_data: dict):
    if not graph_data or not graph_data.get("nodes"):
        st.warning("No knowledge graph data to display.")
        return

    nodes = []
    edges = []
    
    for node_data in graph_data.get("nodes", []):
        nodes.append(
            Node(
                id=node_data.get("id"),
                label=node_data.get("id"),
                title=node_data.get("type"),
                shape="dot",
                color="#00A3E0" # Your theme's primary color
            )
        )

    for edge_data in graph_data.get("edges", []):
        edges.append(
            Edge(
                source=edge_data.get("source"),
                target=edge_data.get("target"),
                label="",
                arrows="to"
            )
        )

    # Config for a dark-mode, physics-enabled graph
    config = Config(
        width=750,
        height=500,
        directed=True,
        physics=True,
        hierarchical=False,
        nodeHighlightBehavior=True,
        highlightColor="#F8F8F8", # Bright white on hover
        
        # --- THIS IS THE FIX ---
        node={'color': '#444444', # Dim gray for the edge line
            'font': {'color': '#888888', 'size': 10}}, # Bright text for nodes
        edge={
            'color': '#444444', # Dim gray for the edge line
            'font': {'color': '#888888', 'size': 10} # Dim gray, smaller font for 'has_tag'
        }
        # --- END OF FIX ---
    )
    
    with st.container(border=True):
        agraph(nodes=nodes, edges=edges, config=config)