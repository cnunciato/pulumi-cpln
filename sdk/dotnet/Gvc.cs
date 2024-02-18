// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;
using Pulumi;

namespace Pulumiverse.Cpln
{
    [CplnResourceType("cpln:index/gvc:Gvc")]
    public partial class Gvc : global::Pulumi.CustomResource
    {
        [Output("alias")]
        public Output<string> Alias { get; private set; } = null!;

        [Output("controlplaneTracing")]
        public Output<Outputs.GvcControlplaneTracing?> ControlplaneTracing { get; private set; } = null!;

        [Output("cplnId")]
        public Output<string> CplnId { get; private set; } = null!;

        [Output("description")]
        public Output<string?> Description { get; private set; } = null!;

        [Output("domain")]
        public Output<string?> Domain { get; private set; } = null!;

        [Output("env")]
        public Output<ImmutableDictionary<string, string>?> Env { get; private set; } = null!;

        [Output("lightstepTracing")]
        public Output<Outputs.GvcLightstepTracing?> LightstepTracing { get; private set; } = null!;

        [Output("loadBalancer")]
        public Output<Outputs.GvcLoadBalancer?> LoadBalancer { get; private set; } = null!;

        [Output("locations")]
        public Output<ImmutableArray<string>> Locations { get; private set; } = null!;

        [Output("name")]
        public Output<string> Name { get; private set; } = null!;

        [Output("otelTracing")]
        public Output<Outputs.GvcOtelTracing?> OtelTracing { get; private set; } = null!;

        [Output("pullSecrets")]
        public Output<ImmutableArray<string>> PullSecrets { get; private set; } = null!;

        [Output("selfLink")]
        public Output<string> SelfLink { get; private set; } = null!;

        [Output("sidecar")]
        public Output<Outputs.GvcSidecar?> Sidecar { get; private set; } = null!;

        [Output("tags")]
        public Output<ImmutableDictionary<string, string>?> Tags { get; private set; } = null!;


        /// <summary>
        /// Create a Gvc resource with the given unique name, arguments, and options.
        /// </summary>
        ///
        /// <param name="name">The unique name of the resource</param>
        /// <param name="args">The arguments used to populate this resource's properties</param>
        /// <param name="options">A bag of options that control this resource's behavior</param>
        public Gvc(string name, GvcArgs? args = null, CustomResourceOptions? options = null)
            : base("cpln:index/gvc:Gvc", name, args ?? new GvcArgs(), MakeResourceOptions(options, ""))
        {
        }

        private Gvc(string name, Input<string> id, GvcState? state = null, CustomResourceOptions? options = null)
            : base("cpln:index/gvc:Gvc", name, state, MakeResourceOptions(options, id))
        {
        }

        private static CustomResourceOptions MakeResourceOptions(CustomResourceOptions? options, Input<string>? id)
        {
            var defaultOptions = new CustomResourceOptions
            {
                Version = Utilities.Version,
                PluginDownloadURL = "github://api.github.com/pulumiverse",
            };
            var merged = CustomResourceOptions.Merge(defaultOptions, options);
            // Override the ID if one was specified for consistency with other language SDKs.
            merged.Id = id ?? merged.Id;
            return merged;
        }
        /// <summary>
        /// Get an existing Gvc resource's state with the given name, ID, and optional extra
        /// properties used to qualify the lookup.
        /// </summary>
        ///
        /// <param name="name">The unique name of the resulting resource.</param>
        /// <param name="id">The unique provider ID of the resource to lookup.</param>
        /// <param name="state">Any extra arguments used during the lookup.</param>
        /// <param name="options">A bag of options that control this resource's behavior</param>
        public static Gvc Get(string name, Input<string> id, GvcState? state = null, CustomResourceOptions? options = null)
        {
            return new Gvc(name, id, state, options);
        }
    }

    public sealed class GvcArgs : global::Pulumi.ResourceArgs
    {
        [Input("controlplaneTracing")]
        public Input<Inputs.GvcControlplaneTracingArgs>? ControlplaneTracing { get; set; }

        [Input("description")]
        public Input<string>? Description { get; set; }

        [Input("domain")]
        public Input<string>? Domain { get; set; }

        [Input("env")]
        private InputMap<string>? _env;
        public InputMap<string> Env
        {
            get => _env ?? (_env = new InputMap<string>());
            set => _env = value;
        }

        [Input("lightstepTracing")]
        public Input<Inputs.GvcLightstepTracingArgs>? LightstepTracing { get; set; }

        [Input("loadBalancer")]
        public Input<Inputs.GvcLoadBalancerArgs>? LoadBalancer { get; set; }

        [Input("locations")]
        private InputList<string>? _locations;
        public InputList<string> Locations
        {
            get => _locations ?? (_locations = new InputList<string>());
            set => _locations = value;
        }

        [Input("name")]
        public Input<string>? Name { get; set; }

        [Input("otelTracing")]
        public Input<Inputs.GvcOtelTracingArgs>? OtelTracing { get; set; }

        [Input("pullSecrets")]
        private InputList<string>? _pullSecrets;
        public InputList<string> PullSecrets
        {
            get => _pullSecrets ?? (_pullSecrets = new InputList<string>());
            set => _pullSecrets = value;
        }

        [Input("sidecar")]
        public Input<Inputs.GvcSidecarArgs>? Sidecar { get; set; }

        [Input("tags")]
        private InputMap<string>? _tags;
        public InputMap<string> Tags
        {
            get => _tags ?? (_tags = new InputMap<string>());
            set => _tags = value;
        }

        public GvcArgs()
        {
        }
        public static new GvcArgs Empty => new GvcArgs();
    }

    public sealed class GvcState : global::Pulumi.ResourceArgs
    {
        [Input("alias")]
        public Input<string>? Alias { get; set; }

        [Input("controlplaneTracing")]
        public Input<Inputs.GvcControlplaneTracingGetArgs>? ControlplaneTracing { get; set; }

        [Input("cplnId")]
        public Input<string>? CplnId { get; set; }

        [Input("description")]
        public Input<string>? Description { get; set; }

        [Input("domain")]
        public Input<string>? Domain { get; set; }

        [Input("env")]
        private InputMap<string>? _env;
        public InputMap<string> Env
        {
            get => _env ?? (_env = new InputMap<string>());
            set => _env = value;
        }

        [Input("lightstepTracing")]
        public Input<Inputs.GvcLightstepTracingGetArgs>? LightstepTracing { get; set; }

        [Input("loadBalancer")]
        public Input<Inputs.GvcLoadBalancerGetArgs>? LoadBalancer { get; set; }

        [Input("locations")]
        private InputList<string>? _locations;
        public InputList<string> Locations
        {
            get => _locations ?? (_locations = new InputList<string>());
            set => _locations = value;
        }

        [Input("name")]
        public Input<string>? Name { get; set; }

        [Input("otelTracing")]
        public Input<Inputs.GvcOtelTracingGetArgs>? OtelTracing { get; set; }

        [Input("pullSecrets")]
        private InputList<string>? _pullSecrets;
        public InputList<string> PullSecrets
        {
            get => _pullSecrets ?? (_pullSecrets = new InputList<string>());
            set => _pullSecrets = value;
        }

        [Input("selfLink")]
        public Input<string>? SelfLink { get; set; }

        [Input("sidecar")]
        public Input<Inputs.GvcSidecarGetArgs>? Sidecar { get; set; }

        [Input("tags")]
        private InputMap<string>? _tags;
        public InputMap<string> Tags
        {
            get => _tags ?? (_tags = new InputMap<string>());
            set => _tags = value;
        }

        public GvcState()
        {
        }
        public static new GvcState Empty => new GvcState();
    }
}